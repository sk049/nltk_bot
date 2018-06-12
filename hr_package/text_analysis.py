import json
import nltk
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer
from nltk.tokenize import word_tokenize
from hr_package import utils as UTILS



with open('/Users/B0097044/Documents/workspace/DummyTraining.json', 'r') as f:
    datastore = json.load(f)


def getLengthOfTrainedData(data):
    dataLength = len(data)
    return dataLength


lengthOfTrainedData = getLengthOfTrainedData(datastore)


stop_words = set(stopwords.words('english'))
#file_data = open("/Users/b0205400/Documents/ChatFile.txt")
#data = file_data.readlines()
str = " "
# for line in data:






# tokens = nltk.word_tokenize(str)


def removeSpecialCharacters(listOfTokens):
    new_tokens = []
    for token in listOfTokens:
        if token != "," and token !=".":
            new_tokens.append(token)

    return new_tokens


#modifiedTokens = removeSpecialCharacters(tokens)


def getWeight(data):
    total_weight = 0
    for response in data:
        total_weight += response['weight']
    return total_weight


def getLength(sentence):
    listOfWords = sentence.split(" ")
    return len(listOfWords);


def removeStopWords(listOfTokens):
    filtered_data = []
    for word in listOfTokens:
        if word not in stop_words:
            filtered_data.append(word)
    return filtered_data


ps = PorterStemmer()


def updateDic(updatedTokens):
    dic = dict()
    for token in updatedTokens:
        print(token.lower())
        if token.lower() not in datastore:
            print("not exist")
        else:
            stemmedWord = token.lower()
            res = datastore[stemmedWord]
            totalWeightofRes = getWeight(res)
            for i in range(len(res)):
                if res[i]['response'] in dic:
                    avgWeight = res[i]['weight']/totalWeightofRes
                    res[i]['weight'] += avgWeight
                    dic[res[i]['response']] = res[i]['weight']
                    i += 1
                else:
                    weight = res[i]['weight']/totalWeightofRes
                    dic[res[i]['response']] = weight
        return dic


def getResponse(dictionary):
    str = " "
    value = 0
    for key in dictionary:
        if dictionary[key] >= value:
            value = dictionary[key]
            str = key
    return str;


def getresponseOfQuery(queryMessage):
    messageTokens = word_tokenize(queryMessage)
    updatedTokens = removeStopWords(removeSpecialCharacters(messageTokens))
    resDic = updateDic(updatedTokens)
    respOfQuery = getResponse(resDic)
    return respOfQuery


queryOfChat = []
responseOfQuery = []



