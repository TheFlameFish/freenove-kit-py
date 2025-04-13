# Modification of project 6.1, using PWM to change the volume of the active buzzer
from gpiozero import Buzzer, Button, PWMOutputDevice
import time

buzzer = PWMOutputDevice("GPIO17", frequency= 1000, initial_value= 0.0)
button = Button("GPIO18")

def cleanup():
    buzzer.close()
    button.close()

def onButtonPressed():
    buzzer.value = 0.15
    print("Button pressed. Buzzer enabled")

def onButtonReleased():
    buzzer.off()
    print("Button released. Buzzer disabled")

def main():
    button.when_activated = onButtonPressed
    button.when_deactivated = onButtonReleased
    while True:
        time.sleep(1)

if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        pass
    finally:
        cleanup()