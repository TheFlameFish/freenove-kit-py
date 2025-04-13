# Project 6.2
from gpiozero import TonalBuzzer, Button
from gpiozero.tones import Tone
import time
import math

buzzer = TonalBuzzer("GPIO17")
button = Button("GPIO18", bounce_time= 0.05)

def cleanup():
    buzzer.close()
    button.close()

def alertor():
    import math
import time

def alertor(): # Modified because the version in the manual didn't work
    for x in range(0, 180):
        if not button.is_active:
            return
        sinVal = math.sin(x * math.pi / 180)
        toneVal = 440 + sinVal * 220  # Oscillate between 220 and 660 Hz
        buzzer.play(Tone(math.floor(toneVal)))
        time.sleep(0.01) 


def stopAlertor():
    time.sleep(0.002)
    buzzer.stop()

def main():
    while True:
        if button.is_active:
            alertor()
        else:
            stopAlertor()

if __name__ == '__main__':
    print("Program starting")
    try:
        main()
    except KeyboardInterrupt:
        pass
    finally:
        cleanup()