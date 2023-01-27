import requests

print(requests.__version__)
# response = requests.get("https://google.com")

response2 = requests.get("https://github.com/qye18/CMPUT404lab1")
print(response2.text)
