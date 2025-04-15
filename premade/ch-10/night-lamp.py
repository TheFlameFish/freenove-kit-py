# Project 10.1, modified
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

def get_light_value():
    value = adc.analogRead(0)
    return -(value / 255) + 1

def get_light_value_processed():
    global dial_values

    value = get_light_value()
    dial_values.insert(0, value)
    dial_values = dial_values[:49]

    avg_value = sum(dial_values) / len(dial_values)

    DARK_THRESHOLD = 0.6  # Below this, LED starts turning on
    FADE_RANGE = 0.2      # Fade in over this range

    brightness = (avg_value - DARK_THRESHOLD) / FADE_RANGE
    brightness = max(0.0, min(brightness, 1.0))

    return brightness


def loop():
    while True:
        dial_value = get_light_value_processed()
        led.value = dial_value
        print(f"Light at {dial_value*100}%")
        print(f"Raw: {get_light_value()}")
        time.sleep(0.03)

if __name__ == "__main__":
    try:
        setup()
        loop()
    except KeyboardInterrupt:
        pass
    finally:
        cleanup()