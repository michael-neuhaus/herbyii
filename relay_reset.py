import RPi.GPIO as GPIO
import time
 # GPIO Nummern statt Board Nummern

pin1 = 11 #luftpumpe
pin2 = 13 #nuescht
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


GPIO.output(pin1,1)
GPIO.output(pin4,1)
GPIO.output(pin5,1)# an
GPIO.output(pin6,1)
GPIO.output(pin7,1)
GPIO.output(pin8,1)

