# Write a program that retrieves the dataset for the "exchequer account (historical series)" from the CSO, 
# and stores it into a file called "cso.json"

# Author: Andrew Scott

import requests
import json

url = "https://ws.cso.ie/public/api.restful/PxStat.Data.Cube_API.ReadDataset/FIQ02/JSON-stat/1.0/en"

# Get the data from the cso website
def get_data():
    response = requests.get(url)
    return response.json()

# Call the function to get data and write to json file
if __name__ == "__main__":
    with open("cso.json", "wt") as fp:
        print(json.dumps(get_data()), file=fp)

