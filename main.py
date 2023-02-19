import time
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)

GPIO.setup(2, GPIO.OUT)
#GPIO.setup(3, GPIO.IN)


def loop():
    while True:
        GPIO.output(2, True)
        print("up")
        time.sleep(0.01)
        GPIO.output(2, False)
        print("down")
        time.sleep(0.01)


if __name__ == "__main__":
    try:
        loop()
    except KeyboardInterrupt:
        GPIO.cleanup()
        exit(1)
