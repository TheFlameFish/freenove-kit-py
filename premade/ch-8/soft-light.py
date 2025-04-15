# Project 8.1, modified
from gpiozero import PWMLED
import time
from ADCDevice import *

led = PWMLED(17, frequency=1000)
adc = ADCDevice()

dial_values = []

def setup():
    global adc
    if (adc.detectI2C(0x48)):
        adc = PCF8591()
    elif (adc.detectI2C(0x4b)):
        adc = ADS7830()
    else:
        print("No correct I2C address found, \n",
              "Pleaseuse command `i2cdetect -y 1` to check the I2C address! \n",
              "Program Exit \n")
        exit(-1)

def cleanup():
    adc.close()
    led.close()

def get_dial_value():
    value = adc.analogRead(0)
    return -(value / 255) + 1

def get_dial_value_averaged():
    global dial_values

    value = get_dial_value()
    dial_values.insert(0, value)
    dial_values = dial_values[:14]

    total: float = 0
    for o in dial_values:
        total += o
    return round(total / len(dial_values), 2)

def loop():
    while True:
        dial_value = get_dial_value_averaged()
        led.value = dial_value
        print(f"Dial turned to {dial_value*100}%")
        time.sleep(0.03)

if __name__ == "__main__":
    try:
        setup()
        loop()
    except KeyboardInterrupt:
        pass
    finally:
        cleanup()