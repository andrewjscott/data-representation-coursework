#  Write a program in another file that works out the average book price from all the books on the server
# Author: Andrew Scott

import requests

url = "http://andrewbeatty1.pythonanywhere.com/books"

def readbooks():
    response = requests.get(url)
    return response.json()

# Gets the average price of all books
def getprice():
    books = readbooks()
    total = 0
    count = 0
    for book in books:
        total += book["Price"]
        count += 1
    return total/count

if __name__ == "__main__":
    avgprice = round(getprice(), 2)
    print("The average price of all books is", avgprice)