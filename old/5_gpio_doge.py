import urllib.request, json 
import RPi.GPIO as GPIO
import time


pinRelay = 20
delay = 0.5
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(pinRelay, GPIO.OUT)

#state = True

def getBalance():
    with urllib.request.urlopen("https://dogechain.info/api/v1/address/balance/DAmSVz4nReXitgHxgZnwyjX5djabEb5qEn") as url:
            data = json.loads(url.read().decode())
            print('got balance ' + data['balance'])
            return data['balance']

initialBalance = getBalance()

while True:
    currentBalance = getBalance()
    if currentBalance > initialBalance:
        initialBalance = currentBalance
        GPIO.output(pinRelay, True)
        time.sleep(delay)
        GPIO.output(pinRelay, False)
        time.sleep(delay)
    time.sleep(3)
