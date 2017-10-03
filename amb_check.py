import requests

token_contract = ""
function_signature = "70a08231000000000000000000000000"
address_to_check = ""

payload = {
    'jsonrpc': '2.0',
    'method': 'eth_call',
    'params': [{
        'to': '0x' + token_contract,
        'data': '0x' + function_signature + address_to_check
    }, 'latest'],
    'id': 1
}

resp = requests.post('http://:443', json=payload)
print(resp)
print(resp.json())
print('balance is {0} ambers'.format(int(resp.json()['result'], 16)))

# print(re.search(r"(?i)(arr|avast|yohoho)!", 'i arr'))
# print('aa{} fff {}d'.format(22, 33))
