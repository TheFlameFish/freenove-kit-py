from gpiozero import LED
from time import sleep

led = LED("GPIO17") # Physical number: 11

def main():
    n: int = None
    while n is None:
        try:
            _n = int(input("n: "))
            assert(_n >= 1)
            n = _n
        except (ValueError, AssertionError):
            print("Please enter a positive non-zero integer.")

    frequency: float = None
    while frequency is None:
        try:
            _frequency = float(input("Frequency (Hz): "))
            assert(_frequency > 0)
            frequency = _frequency
        except (ValueError, AssertionError):
            print("Please enter a positive non-zero float.")

    led.blink(n = n, background = False, on_time= (1/frequency)/2, off_time= (1/frequency)/2)

if __name__ == '__main__':
    print("Program starting\n")
    try:
        main()
    except KeyboardInterrupt:
        print("Exiting")
    finally:
        led.close()