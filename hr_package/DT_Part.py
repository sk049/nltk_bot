import json
from flask import jsonify



commonPath = "/Users/b0205400/Downloads/"


def getPath(fileName):
    fileLocation = commonPath +fileName+".json"
    return fileLocation



def getResponse(scenario):
    datas = []
    filePath = getPath(scenario)
    print(filePath)

    with open(filePath, 'r') as f:

        datas = json.load(f)
        print(datas)
    return datas




