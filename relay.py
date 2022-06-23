import RPi.GPIO as GPIO
import time
 # GPIO Nummern statt Board Nummern

pin1 = 11
pin2 = 22
pin3 = 12
pin4 = 3
pin5 = 2
pin6 = 1

GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)
GPIO.setup(pin1, GPIO.OUT) # GPIO Modus zuweisen
GPIO.output(pin1, 0) # aus
time.sleep(5)
GPIO.output(pin1, 1) # an
time.sleep(5)
GPIO.output(pin1, 0)
time.sleep(5)
GPIO.output(pin1, 0)
time.sleep(5)
GPIO.output(pin1, 1)