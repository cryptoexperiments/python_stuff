import time
import requests
# import RPi.GPIO as GPIO
NODE_ADDRESS = 'http://'
TOKEN_CONTRACT = ''
FUNCTION_SIGNATURE = ''
ADDRESS_TO_CHECK = ''
ITEM_PRICE = 5

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


def perform_action():
    print("performing action")
    # GPIO.setwarnings(False)
    # GPIO.setmode(GPIO.BCM)
    # GPIO.setup(17, GPIO.OUT)
    # GPIO.setup(20, GPIO.OUT)
    # GPIO.output(17, True)
    # GPIO.output(20, True)
    # time.sleep(1)
    # GPIO.output(17, False)
    # GPIO.output(20, False)


perform_action()  # just to test
initial_balance = get_balance()

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
    time.sleep(10)


