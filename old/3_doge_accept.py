import urllib.request, json 
import time

##with urllib.request.urlopen("http://maps.googleapis.com/maps/api/geocode/json?address=google") as url:
##    data = json.loads(url.read().decode())
##    print(data)

##9yx9cbftsrBwGQ4Fa8fADLsUgpsZQYdhNp
while True:
    with urllib.request.urlopen("https://dogechain.info/api/v1/address/balance/DAmSVz4nReXitgHxgZnwyjX5djabEb5qEn") as url:
        data = json.loads(url.read().decode())
    ##    print(data)
        print(data['balance'])
        time.sleep(2)
