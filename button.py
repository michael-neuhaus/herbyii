import RPi.GPIO as GPIO
import time
from buzz import *
import os



pin1 = 11 # luftpumpe
pin2 = 13 # nuescht
pin3 = 15 # nuescht
pin4 = 19 # licht
pin5 = 21 # Kreis 1
pin6 = 23 # Pumpe Rein [80]
pin7 = 10 # Pumpe Raus [35]
pin8 = 12 # Kreis 2

GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)

GPIO.setup(pin1, GPIO.OUT) # GPIO Modus zuweisen
GPIO.setup(pin7, GPIO.OUT)
GPIO.setup(pin8, GPIO.OUT)
GPIO.setup(pin4, GPIO.OUT)
GPIO.setup(pin5, GPIO.OUT)
GPIO.setup(pin6, GPIO.OUT)

GPIO.setup(38, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

GPIO.output(pin1,0)
GPIO.output(pin4,0)
GPIO.output(pin5,0)
GPIO.output(pin8,0)
GPIO.output(pin7,1)
GPIO.output(pin6,1)



while True:
    if (GPIO.input(38) == 1) :
        print ("Wasserwechsel initialsiert")
        os.system("sudo python3 grove_pwm_buzzer.py")
        GPIO.output(pin5,1)
        GPIO.output(pin8,1)
        GPIO.output(pin7,0)# an
        time.sleep(30)
        GPIO.output(pin7,1)
        GPIO.output(pin6,0)
        time.sleep(75)
        GPIO.output(pin6,1)
        GPIO.output(pin5,0)
        GPIO.output(pin8,0)

        # nur testen
        time.sleep(5)
        GPIO.output(pin5,1)
        GPIO.output(pin8,1)
        # normalzustand wiederherstellung
        
        GPIO.output(pin1,0)
        GPIO.output(pin4,0)
        GPIO.output(pin5,0)
        GPIO.output(pin8,0)
        GPIO.output(pin7,1)
        GPIO.output(pin6,1)
        GPIO.setup(38, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
        os.system("sudo python3 grove_pwm_buzzer.py")
        print("wasswerchsel beendet")
    print("button nicht gedrückt")    
    time.sleep(.5)