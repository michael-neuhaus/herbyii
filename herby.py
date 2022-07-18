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
    
# def email_alert(mois,tds,light,temp,humi):
    
    # if (temp < 18 or temp > 25):
    
    # if (mois < 1000 or mois > 2000):
 
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
                
                
        os.system('git add .')
        os.system('git commit -m "auto push"')
        os.system('git push')
        
        display_data_on_console(tds,light,temp,humid)
        # display_data_on_lcd(tds,light,temp,humid)
        
        # display data on lcd
        # takes 30 minutes
        for i in range(0,72):
            # takes 25 seconds
            display_data_on_lcd(tds,light,temp,humid)
        
        # TO DO:
        # check if any sensor value is out of recommended range
        # send email alert if that is the case
        # return
        
        # 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
        
        # time.sleep(12)

if __name__ == '__main__':
    main()

