import requests

app = requests.get("https://staging.api.tzkt.io/v1/accounts")
a = app.text
print(app.text)
