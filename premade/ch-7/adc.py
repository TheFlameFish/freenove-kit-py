import time
from ADCDevice import *

# This has no built-in documentation .-.
adc = ADCDevice()

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

def loop():
    while True:
        value = adc.analogRead(0) # Read channel 0
        voltage = (value / 255.0 * 3.3) # Read output will be zero to 255. Convert to 0.0 to 1.0, then to 0.0 to 3.3 (max voltage).
        percent = -((value / 255.0) * 100) + 100
        print(f"ADC Value: {value:<10} Voltage: {voltage:<10.2f} Percent: {percent:.2f}%")
        time.sleep(0.1)

if __name__ == "__main__":
    try:
        setup()
        loop()
    except KeyboardInterrupt:
        pass
    finally:
        cleanup()