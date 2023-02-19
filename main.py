import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)

GPIO.setup(2, GPIO.OUT)
#GPIO.setup(3, GPIO.IN)


def loop():
    while True:
        GPIO.output(2, True)
        GPIO.output(3, False)


if __name__ == "__main__":
    try:
        loop()
    except KeyboardInterrupt:
        exit(1)
