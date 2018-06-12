import xlrd
import json

commonPath = "/Users/B0097044/Downloads/"
filePath = commonPath + "leave.xls"
wb = xlrd.open_workbook(filePath)

sheet = wb.sheet_by_name('leave')
print(sheet)

ScenarioDict = {}
count = 1
print(sheet.nrows)
for rownum in range(sheet.nrows):
    if rownum > 0:
        if count in range(sheet.nrows):
            rowValues = sheet.row_values(count)
            str = ""+rowValues[0]
            ScenarioDict[str] = {}
            ScenarioDict[str]['scenario'] = rowValues[2]
            list = []
            localdict = {}
            localdict['choiceValue'] = rowValues[5]
            localdict['nextStep'] =  rowValues[8]
            list.append(localdict)
            emptyString = ""
            nextRow = rownum+1
            if nextRow in range(sheet.nrows):
                while sheet.row_values(nextRow)[0] == emptyString:
                    newDict = {}
                    newDict['choiceValue'] = sheet.row_values(nextRow)[5]
                    newDict['nextStep'] =  sheet.row_values(nextRow)[8]
                    list.append(newDict)
                    nextRow += 1
            ScenarioDict[str]['ChoiceValues'] = list
            count = nextRow






with open("/Users/B0097044/Downloads/leave.json",'w') as js:
    json.dump(ScenarioDict,js)






