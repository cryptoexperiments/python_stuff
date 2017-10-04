import http.client
import json
import time
import RPi.GPIO as GPIO


def get_balance():
    conn = http.client.HTTPSConnection("mainnet.infura.io")
    # token_contract = "0xa74476443119A942dE498590Fe1f2454d7D4aC0d"  # GNT token
    token_contract = "0xd26114cd6EE289AccF82350c8d8487fedB8A0C07"  # OMG token
    function_signature = "70a08231000000000000000000000000"  # get balance signature

    address_to_check = "fbb1b73c4f0bda4f67dca266ce6ef42f520fbb98"  # address with lot of OMG activity
    # address_to_check = "7fe2b88f2e4858de375832fbf54ac7cf1a78ca51"  # address with lot of GNT activity

    payload = {
        "jsonrpc": "2.0",
        "method": "eth_call",
        "params": [{
            "to": token_contract,
            "data": "0x" + function_signature + address_to_check
        }, "latest"],
        "id": 1
    }

    # type = dict
    headers = {
        'content-type': "application/json",
        'cache-control': "no-cache"
    }

    conn.request("POST", "/", json.dumps(payload), headers)
    res = conn.getresponse()
    response_data = res.read()
    print("response raw data:")
    print(response_data.decode("utf-8"))  # bytes decoded to str

    json_response_data = json.loads(response_data.decode("utf-8"))
    print("json_response_data:")
    print(json_response_data)

    print("result(hex):")
    print(json_response_data['result'])

    print("result(decimal):")
    # print(int(json_response_data['result'], 16))
    result = int(json_response_data['result'], 16) / 1000000000000000000
    print(result)
    return result


def perform_action():
    print("performing action")
    GPIO.setwarnings(False)
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(17, GPIO.OUT)
    GPIO.setup(20, GPIO.OUT)
    GPIO.output(17, True)
    GPIO.output(20, True)
    time.sleep(1)
    GPIO.output(17, False)
    GPIO.output(20, False)


perform_action()  # just to test
initialBalance = get_balance()
while True:
    currentBalance = get_balance()
    if currentBalance != initialBalance:
        print("!!! balance changed !!!")
        initialBalance = currentBalance
        perform_action()
        # do stuff
        # time.sleep(delay)
        # time.sleep(delay)
    time.sleep(3)
