import time
from datetime import date
import json

import os

# sensor imports
from grove.grove_moisture_sensor import GroveMoistureSensor
from grove.display.jhd1802 import JHD1802
from TDS import GroveTDS
from grove.grove_light_sensor_v1_2 import GroveLightSensor
from seeed_dht import DHT

# email imports
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders


  
# tds sensor     
def tds_sensor():
        sensor_tds = GroveTDS(0)
        return round(sensor_tds.TDS)
        
# light       
def light_sensor():
        sensor = GroveLightSensor(2)
        return sensor.light
        
# temperature 
def temp_and_humid_sensor():

    # find correct port in base hat
    sensor = DHT('11', 5)
    
    # read sensor values
    humidity, temp = sensor.read()        
    return humidity, temp

def write_json(new_data, filename="sample.json"):
    
    with open(filename,"r+") as file:
        file_data = json.load(file)
        file_data["herby_details"].append(new_data)
        file.seek(0)
        json.dump(file_data, file, indent =6)
        
# display sensor data on lcd    
def display_data_on_lcd(tds,light,temp,humid):
    
    lcd = JHD1802()

    lcd.setCursor(0,0)
    lcd.write('tds: {}'.format(tds))
    time.sleep(5)
    
    lcd.setCursor(0,0)
    lcd.write('light: {}'.format(light))
    time.sleep(5)
    
    lcd.setCursor(0,0)
    lcd.write('temperature: {}C'.format(temp))
    time.sleep(5)
    
    lcd.setCursor(0,0)
    lcd.write('humidity: {}%'.format(humid))
    time.sleep(5)
    
def display_data_on_console(tds,light,temp,humid):
    
    print("TDS: ", tds)
    print("light: ", light)
    print("temperature: ",temp)
    print("humidity: ", humid)
    
def email_alert(tds,light,temp, current_time):
    
    # check if value is out of bounds 
    if (tds < 500 or light < 500 or temp < 18 or temp > 25):
        # check hours and minutes of current time to only send one email per day
        # only sends between 06:00 and 06:30
        if (int(current_time[0]) == 0 and int(current_time[1]) == 6):
            if (int(current_time[3])*10 + int(current_time[4]) < 30):
                
                email_user = "herbyalert@gmail.com"
                email_password = "rpytmofsaefwytuw"
                email_send = "michael.neuhaus97@gmail.com"

                subject = "herby alert"

                msg = MIMEMultipart()
                msg["From"] = email_user
                msg["To"] = email_send
                msg["Subject"] = subject

                body = "One of herby's sensors has measured a value out of the recommended range."
                msg.attach(MIMEText(body,"plain"))

                text = msg.as_string()
                server = smtplib.SMTP("smtp.gmail.com",587)
                server.starttls()
                server.login(email_user,email_password)

                server.sendmail(email_user,email_send,text)
                server.quit()
 
def main():
    
    # Kann als eingestaendige Funktion geshhrieben werde
    # TO-DO
    jsonInitializeData = {
        "herby_details": [
        ]
    }
    json_herby_ini = json.dumps(jsonInitializeData, indent = 6)
    with open("sample.json","w") as outfile:
        outfile.write(json_herby_ini)
        
    while True:
        
        # current date and time
        currentDate = date.today()
        today = currentDate.strftime('%m/%d/%y')
        t = time.localtime()
        current_time = time.strftime("%H:%M:%S", t)

        # call all sensors
        tds = tds_sensor()
        light = light_sensor()
        humid, temp = temp_and_humid_sensor()
        
        # prepare data to write in file
        data = {
            "tds": tds,
            "light" : light,
            "temperature" : temp,
            "humidity" : humid,
            "date" : today,
            "time" : current_time,
        }
        
        write_json(data)
        
        # convert json to js file
        with open('sample.json') as file:
            data = json.loads(file.read())
            with open("sensor_data.js", 'w') as file:
                file.write("const sensor_data =" + str(data))
                
                
        # os.system('git add .')
        # os.system('git commit -m "auto push"')
        # os.system('git push')
        
        display_data_on_console(tds,light,temp,humid)
        
        email_alert(tds,light,temp, current_time)
        
        # display data on lcd
        # takes 30 minutes
        for i in range(0,72):
            # takes 25 seconds
            display_data_on_lcd(tds,light,temp,humid)
            
        # send email if a value out of bounds
        
        
        # time.sleep(12)

if __name__ == '__main__':
    main()


