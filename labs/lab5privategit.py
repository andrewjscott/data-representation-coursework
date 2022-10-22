# Get private data from GitHub
import requests
import json
from config import config as cfg

url = "https://api.github.com/repos/andrewjscott/aprivateone"
api_key = cfg["git_key"]
filename = "priv_repo.json"

response = requests.get(url, auth = ("token", api_key))

repoJSON = response.json()
#print(response.json())

with open(filename, "w") as fp:
    json.dump(repoJSON, fp, indent=4)


