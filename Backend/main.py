import requests
from database.models import user, write, read


MAIN = "https://api.hangzhou.tzstats.com"
ACCOUNT = "/explorer/account/"
ACCOUNT_OPERATION = "/operations"
TOKEN = 0

def return_account(id):
    TOKEN = id
    a = requests.get(MAIN+ACCOUNT+TOKEN)
    return a.text

def return_account_operation(id):
    TOKEN = id
    a = requests.get(MAIN+ACCOUNT+TOKEN+ACCOUNT_OPERATION)
    return a.text

users = return_account_operation("tz1bPmDANudr2SjSyg6MY5kBsdSMY3Xiirat")
a = user.insert().values(
    data=users
)

write(a)

data = read(user)


