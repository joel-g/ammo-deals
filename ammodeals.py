import requests

res = requests.get('https://ammoseek.com/go.to/54376990606')
print(res)
print(dir(res))
print(res.text)