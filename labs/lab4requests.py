# write a module to interact with the API created at http://andrewbeatty1.pythonanywhere.com/books

import requests

# Test to see if requests is working. should get a whole pile of html
# url = "http://google.com"
# response = requests.get(url)
# print(response.text)

url = "http://andrewbeatty1.pythonanywhere.com/books"

def readbooks():
    response = requests.get(url)
    return response.json()

def readbook(id):
    geturl = url + "/" + str(id)
    response = requests.get(geturl)
    return response.json()

def createbook(book):
    response = requests.post(url, json=book)
    return response.json()

def updatebook(id, book):
    puturl = url + "/" + str(id)
    response = requests.put(puturl, json=book)
    return response.json()

def deletebook(id):
    deleteurl = url + "/" + str(id)
    response = requests.delete(deleteurl)
    return response.json()


if __name__ == "__main__":
    print(readbooks())

