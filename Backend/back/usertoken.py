import requests

""""
tz1bPmDANudr2SjSyg6MY5kBsdSMY3Xiirat

https://api.tzkt.io/v1/accounts
"""

class Token:
    def __init__(self, token):
        self.token = token

    def get_token(self):
        account = requests.get("https://api.tzkt.io/v1/accounts/{0}".format(self.token)).json()
        return account

    def get_account(self ):
        token = self.get_token()
        if "address" in token:
            #if token["address"] != '':
            return token["address"]
        else:
            print("Неверный токен")
            return 0

    def get_balance_account(self):
        if self.get_token() != 0:
            balance = self.get_token()
            return balance["balance"]
        else:
            return 0


       #a = str(balance[0])
        #for i in a.split(","):
         #   print(i)


'''a = Token('tz1Td6zHZHrMRGvaZNTvBDsKrnGA2GrG647m')
a.get_account()
a.get_account()
a.get_balance_account()
'''

'''app = requests.get("https://api.tzkt.io/v1/accounts").text
for i in app.split(","):
    print(i)

apps = requests.get("https://api.tzkt.io/v1/accounts/tz1hgkiVecL3zzsfxwZf43KRrvrTbVZtPerM/operations").text
'''


"""{"type":"user"
"address":"tz1Ke2h7sDdakHJQh8WX4Z372du1KChsksyU"
"alias":"Null-address"
"revealed":false
"balance":27931970860
"counter":20716301
"numContracts":34
"activeTokensCount":26
"tokenBalancesCount":26
"tokenTransfersCount":40
"numActivations":0
"numDelegations":0
"numOriginations":0
"numTransactions":29425
"numReveals":0
"numRegisterConstants":0
"numMigrations":0
"firstActivity":1
"firstActivityTime":"2018-06-30T17:39:57Z"
"lastActivity":2123460
"lastActivityTime":"2022-02-16T19:32:00Z"}"""