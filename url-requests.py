# Playing with URL requests
# Author: Andrew Scott


import requests

url = "https://reqbin.com/echo"


resp = requests.get(url)

print(resp.status_code)