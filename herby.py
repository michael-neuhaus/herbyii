import time
from mraa import getGpioLookup
from upm import pyupm_buzzer as upmBuzzer
# import pandas as pd
from datetime import date

#Moisture import
from grove.grove_moisture_sensor import GroveMoistureSensor

#display import
from grove.display.jhd1802 import JHD1802

#TDS import
from TDS import GroveTDS

#Light import
from grove.grove_light_sensor_v1_2 import GroveLightSensor

#temperature import
from seeed_dht import DHT

#import for csv file
import csv

#import json for json file

import json

#seperate sensor functions to read and process values, to be called in main
  
#tds and moisture       
def moisture_tds_main():    
        #read sensor values
        sensor = GroveMoistureSensor(4)
        sensor_tds = GroveTDS(0)
        
        #print sensor values
        print('TDS Value: {0}'.format(sensor_tds.TDS))
        
        mois = sensor.moisture
        if 0 <= mois and mois < 300:
            level = 'dry'
        elif 300 <= mois and mois < 600:
            level = 'moist'
        else:
            level = 'wet'
        
        #print values in terminal (level printed in terminal)      
        print('moisture: {}, {}'.format(mois, level)) 
        return mois,sensor_tds.TDS
        
#light       
def Light_main():      
        #read sensor values
        sensor = GroveLightSensor(2)
        #print values in terminal
        print('light value {}'.format(sensor.light))
        
        return sensor.light
        
#temperature 
def temp_main():
        #display
        lcd = JHD1802()
        #find correct port in base hat
        sensor = DHT('11', 5)
        
        #read sensor values
        humi, temp = sensor.read()
        #print values in terminal
        print('temperature {}C, humidity {}%'.format(temp,humi))
            
        #print values on display
        lcd.setCursor(0,0)
        lcd.write('temperature: {0:2}C'.format(temp))
        
        return temp , humi

def write_json(new_data, filename="sample.json"):
    with open(filename,"r+") as file:
        file_data = json.load(file)
        file_data["herby_details"].append(new_data)
        file.seek(0)
        json.dump(file_data, file, indent =4)
        
#main functions calls all sensor functions and writes values in csv file 
def main():
    #Kann als eingeständige Funktion geshhrieben werde
    #TO-DO
    jsonInitializeData = {
        "herby_details": [
        ]
    }
    json_herby_ini = json.dumps(jsonInitializeData, indent = 4)
    with open("sample.json","w") as outfile:
        outfile.write(json_herby_ini)
        
    while True:
        
        time.sleep(5)
        i= 4
        i= i+4

        #call all sensors
        mois,tds = moisture_tds_main()
        light = Light_main()
        temp, humi = temp_main()
        
        data = {
            "moisture": mois,
            "light" : light,
            "temp" : temp,
            "humi" : humi,
        }
        
        write_json(data)
        #hello
        
        #new_data = json.dumps(data, indent = 4)
        
        #with open("sample.json") as f:
         #   old_data = json.load(f)
            
            
        #old_data.update(data)
        
        #json_herby2 = json.dumps(old_data, indent = i)
        
        #with open("sample.json", "w") as outfile:
         #   outfile.write(json_herby2)
        
        
        #get current date in correct format and write all sensor values in file with according date
        currentDate = date.today()
        today = currentDate.strftime('%m/%d/%y')
        toWrite = [mois, light, temp]
        #write_json(toWriteJson)
        #create data frame 
        # df = pd.read_csv('test.csv')
        # df[today] = toWrite
        # df.to_csv('test.csv', index=False)
        #sleep for 24h, programm runs once a day
        
        

if __name__ == '__main__':
    main()
