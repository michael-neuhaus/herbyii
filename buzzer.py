from __future__ import print_function

import time
from mraa import getGpioLookup
from upm import pyupm_buzzer as upmBuzzer

def main():
    print("What up")
    
    pin = 12
    
    mraa_pin = getGpioLookup("GPIO%d" % pin)
    buzzer = upmBuzzer.Buzzer(mraa_pin)
    
    chords = [upmBuzzer.BUZZER_DO, upmBuzzer.BUZZER_RE, upmBuzzer.BUZZER_MI,
              upmBuzzer.BUZZER_FA, upmBuzzer.BUZZER_SOL, upmBuzzer.BUZZER_LA,
              upmBuzzer.BUZZER_SI];
    
    print(buzzer.name())
    
    for chord_ind in range (0,7):
        print(buzzer.playSound(chords[chord_ind], 500000))
        time.sleep(0.1)
        
    del buzzer
    
    print("debug")
    
    if __name__ == '__main__':
        main()