from gpiozero import LED
from time import sleep

led = LED("GPIO17") # Physical number: 11

def main():
    n: int = None
    while not n:
        try:
            _n = int(input("n: "))
            assert(_n >= 1)
            n = _n
        except ValueError:
            print("Please enter a positive non-zero integer.")
        except AssertionError:
            print("Please enter a positive non-zero integer.")

    frequency: float = None
    while not frequency:
        try:
            _frequency = float(input("Frequency (Hz): "))
            assert(_frequency > 0)
            frequency = _frequency
        except ValueError:
            print("Please enter a positive non-zero float.")
        except AssertionError:
            print("Please enter a positive non-zero float.")

    led.blink(n = n, background = False, on_time= (1/frequency)/2, off_time= (1/frequency)/2)

if __name__ == '__main__':
    print("Program starting\n")
    try:
        main()
        led.close()
    except KeyboardInterrupt:
        print("Exiting")
        led.close()