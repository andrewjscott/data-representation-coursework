# Write a program that prints the data for all trains in Ireland to the console.

import requests
import csv
from xml.dom.minidom import parseString

url = "http://api.irishrail.ie/realtime/realtime.asmx/getCurrentTrainsXML"
page = requests.get(url)
doc = parseString(page.content)

# print(doc.toprettyxml())

# if I want to store the xml in a file. You can comment this out later
# with open("trainxml.xml","w") as xmlfp:
#    doc.writexml(xmlfp)


# I had an issue with blank lines in the file so found solution at
# https://stackoverflow.com/questions/3348460/csv-file-written-with-python-has-blank-lines-between-each-row
# adding the newline= '' parameter
with open('week03_train.csv', mode='w', newline='') as train_file:
    train_writer = csv.writer(train_file, delimiter='\t', quotechar='"', quoting=csv.QUOTE_MINIMAL)

    retrieveTags=['TrainStatus',
                'TrainLatitude',
                'TrainLongitude',
                'TrainCode',
                'TrainDate',
                'PublicMessage',
                'Direction'
                ]


    objTrainPositionsNodes = doc.getElementsByTagName("objTrainPositions")
    for objTrainPositionsNode in objTrainPositionsNodes:
        train_lat_node = objTrainPositionsNode.getElementsByTagName("TrainLatitude").item(0)
        train_lat = train_lat_node.firstChild.nodeValue.strip()
        dataList = []
        for retrieveTag in retrieveTags:
            datanode = objTrainPositionsNode.getElementsByTagName(retrieveTag).item(0)
            dataList.append(datanode.firstChild.nodeValue.strip())
        train_writer.writerow(dataList)
        # print (train_lat)

# only store the trains whose traincode starts with a D
import pandas as pd

df = pd.read_csv (r'week03_train.csv', sep='\t')
# print (df)


