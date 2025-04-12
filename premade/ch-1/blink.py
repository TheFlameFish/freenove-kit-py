from gpiozero import LED
from time import sleep

led = LED("GPIO17") # Physical number: 11

def loop():
    while True:
        led.on()
        print("LED enabled")
        sleep(1)
        led.off()
        print("LED disabled")
        sleep(1)

if __name__ == '__main__':
    print("Program starting\n")
    try:
        loop()
    except KeyboardInterrupt:
        print("Exiting")
        led.close()

