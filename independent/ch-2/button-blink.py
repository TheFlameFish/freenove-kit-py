from gpiozero import LED, Button
from time import sleep

led = LED(17)       # define LED pin according to BCM Numbering
button = Button(18, pull_up= True) # define Button pin according to BCM Numbering

def main():
    previous = button.value
    toggle = False

    while True:
        if button.value == False and previous == True: # On button release
            toggle = not toggle
            print("Toggled")
            if toggle:
                led.blink(on_time=0.2, off_time=0.2)
            else:
                led.off()
        previous = button.value
        sleep(0.01)

if __name__ == '__main__':     # Program entrance
    print ('Program is starting...')
    try:
        main()
    except KeyboardInterrupt:  # Press ctrl-c to end the program.
        print("Ending program")
