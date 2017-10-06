import time
import requests
import RPi.GPIO as GPIO
NODE_ADDRESS = 'http://'
TOKEN_CONTRACT = ''
FUNCTION_SIGNATURE = ''
ADDRESS_TO_CHECK = ''
ITEM_PRICE = 5
PIN_BUZZER = 17
PIN_SOLENOID = 27


def get_balance():
    payload = {
        'jsonrpc': '2.0',
        'method': 'eth_call',
        'params': [{
            'to': '0x' + TOKEN_CONTRACT,
            'data': '0x' + FUNCTION_SIGNATURE + ADDRESS_TO_CHECK
        }, 'latest'],
        'id': 1
    }

    resp = requests.post(NODE_ADDRESS, json=payload, timeout=2)
    # print(resp.status_code)
    # print(resp.json())
    result = int(resp.json()['result'], 16)
    print('balance is {0} ambers'.format(result))
    return result


def gpio_init():
    GPIO.setwarnings(False)
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(PIN_BUZZER, GPIO.OUT)
    GPIO.setup(PIN_SOLENOID, GPIO.OUT)
    GPIO.output(PIN_BUZZER, True)
    time.sleep(1)
    GPIO.output(PIN_BUZZER, False)


def perform_action():
    print("performing action")
    GPIO.output(PIN_BUZZER, True)
    GPIO.output(PIN_SOLENOID, True)
    time.sleep(0.5)
    GPIO.output(PIN_BUZZER, False)
    GPIO.output(PIN_SOLENOID, False)


def insufficien_payment():
    for n in range(3):
        GPIO.output(PIN_BUZZER, True)
        time.sleep(0.1)
        GPIO.output(PIN_BUZZER, False)
        time.sleep(0.1)
    

gpio_init()
initial_balance = get_balance()
last_seen_insufficient_balance = 0

while True:
    print("initial balance={}".format(initial_balance))

    try:
        current_balance = get_balance()
    except Exception as e:
        print('Exception catched in:{}'.format(e))
        current_balance = initial_balance  # TODO check if we need this

    if current_balance < initial_balance:
        print("!!! balance decreased !!!")
        # probably device owner moved tokens - resetting initial balance to the current value
        initial_balance = current_balance
    if current_balance > initial_balance:
        print("!!! balance increased !!!")
        if current_balance >= initial_balance + ITEM_PRICE:
            initial_balance += ITEM_PRICE
            perform_action()
        elif current_balance != last_seen_insufficient_balance:
            print("!!! insufficient payment !!!")
            last_seen_insufficient_balance = current_balance
            insufficien_payment()
    time.sleep(0.5)


