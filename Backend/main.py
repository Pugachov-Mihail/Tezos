import requests

MAIN = "https://api.hangzhou.tzstats.com"
ACCOUNT = "/explorer/account/"
ACCOUNT_OPERATION = "/operations"
TOKEN = 0

def return_account(id):
    TOKEN = id
    a = requests.get(MAIN+ACCOUNT+TOKEN)
    return a.content

def return_account_operation(id):
    TOKEN = id
    a = requests.get(MAIN+ACCOUNT+TOKEN+ACCOUNT_OPERATION)
    return a.content

return_account_operation("tz1bPmDANudr2SjSyg6MY5kBsdSMY3Xiirat")

