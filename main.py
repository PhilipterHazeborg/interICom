import time
import RPi.GPIO as GPIO
import threading
import queue

data = 'hello World'
q = queue.Queue()

TX1_pin = 2
clk = 3
GPIO.setmode(GPIO.BCM)
#TX
GPIO.setup(TX1_pin, GPIO.OUT)
#Clock
GPIO.setup(clk, GPIO.OUT)
#RX
#GPIO.setup(3, GPIO.IN)



def convert_to_ascii(input_data: str):
    output = ''.join(str(ord(c)) for c in input_data)
    return output

    
def convert_to_binary(input_data: str):
    output = ''.join('{:08b}'.format(x) for x in bytearray(input_data, 'utf-8'))
    return output


def clock(sleeptime:  float):
    while True:
        GPIO.output(clk, True)
        send_first_of_stack()
        time.sleep(sleeptime)
        GPIO.output(clk, False)
        time.sleep(sleeptime)


def send(data_in):
    for x in data_in:
        if x == "1":
            GPIO.output(TX1_pin, True)
        elif x == "0":
            print(0)
        else:
            print("NaN")


def send_first_of_stack():
    queue_data = q.get()
    print(queue_data)
    if queue_data != "":
        bit_to_transmit = queue_data[0]
        remaining_stack = queue_data[1:]
        if bit_to_transmit == "1":
            GPIO.output(TX1_pin, True)
        elif bit_to_transmit == "0":
            GPIO.output(TX1_pin, False)
        else:
            GPIO.output(TX1_pin, False)
        q.put(remaining_stack)
    

def pull_down():
    GPIO.output(TX1_pin, False)


def main():
    print(convert_to_binary(data))
    q.put(convert_to_binary(data))


if __name__ == "__main__":
    try:
        main()
        t1 = threading.Thread(target=clock, args=(0.01,))
        t1.start()
    except KeyboardInterrupt:
        GPIO.cleanup()
        exit(1)
