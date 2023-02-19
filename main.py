import time
#import RPi.GPIO as GPIO
import threading
data = 'hello World'

#GPIO.setmode(GPIO.BCM)
#RX
#GPIO.setup(2, GPIO.OUT)
#Clock
#GPIO.setup(3, GPIO.OUT)
#TX
#GPIO.setup(3, GPIO.IN)


def convert_to_ascii(input_data: str):
    output = ''.join(str(ord(c)) for c in input_data)
    return output

    
def convert_to_binary(input_data: str):
    output = ' '.join('{:08b}'.format(x) for x in bytearray(input_data, 'utf-8'))
    return output


def clock(sleeptime:  float, clk_pin: int):
    #GPIO.output(clk_pin, True)
    time.sleep(sleeptime)
    #GPIO.output(clk_pin, False)
    time.sleep(sleeptime)


def send():
    while True:
        #GPIO.output(2, True)
        print("up")
        time.sleep(0.01)
        #GPIO.output(2, False)
        print("down")
        time.sleep(0.01)
        
        
def main():
    print(convert_to_binary(data))


if __name__ == "__main__":
    try:
        #t1 = threading.Thread(target=clock, args=(0.01, 3))
        #t2 = threading.Thread(target=send(), args=())
        
        #t1.start()
        #t2.start()
        main()
    except KeyboardInterrupt:
        #GPIO.cleanup()
        exit(1)
