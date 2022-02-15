import requests

""""
tz1bPmDANudr2SjSyg6MY5kBsdSMY3Xiirat

https://api.tzkt.io/v1/accounts
"""

class Token:
    def __init__(self, token):
        self.token = token

    def get_account(self):
        account = requests.get("https://api.tzkt.io/v1/accounts/{0}".format(self.token))
        token = account.json()
        if "address" in token:
            if token["address"] != '':
                return token["address"]
        else:
            print("Неверный токен")
            return 0

    def get_balance_account(self):
        balance = requests.get("https://api.tzkt.io/v1/tokens/balances?accounts={0}=50&balance.gt=0".format(self.get_account())).json()
        a = str(balance[0])
        for i in a.split(","):
            print(i)
        if self.get_account() != 0:
            return balance[0]["balance"]
        else:
            return 0


app = requests.get("https://api.tzkt.io/v1/accounts").text
for i in app.split(","):
    print(i)

apps = requests.get("https://api.tzkt.io/v1/accounts/tz1hgkiVecL3zzsfxwZf43KRrvrTbVZtPerM/operations").text

'''
a = Token('tz1bPmDANudr2SjSyg6MY5kBsdSMY3Xiirat')
a.get_account()
a.get_balance_account()'''