import requests

URL = 'https://google.com'
def lambda_handler():
     r = requests.get(URL)
     return r.status_code

print(lambda_handler())