import json

from flask import jsonify

file_path = '/Users/B0097044/Documents/workspace/'
file_extension = '.json'


def generate_file_path(file_name):
    full_path = file_path + file_name + file_extension
    return full_path;


def return_scenario_response(scenario_id, file_name):
    dic = dict();
    file_read_path = generate_file_path(file_name)
    with open(file_read_path, 'r') as f:
        data_source = json.load(f)
        if scenario_id in data_source:
            response_scenario = data_source[scenario_id]
            dic['response']=response_scenario
            dic['fileName']=file_name
            print(dic)
            return dic


def get_dummy_response(message,identifier):
    with open('/Users/B0097044/Documents/workspace/dummy.json', 'r') as f:
        data_source = json.load(f)
        if identifier in data_source :
            response_scenario = data_source[identifier]
            return response_scenario


def getResponse(scenario):
    datas = []
    filePath = generate_file_path(scenario)
    print(filePath)
    with open(filePath, 'r') as f:
        datas = json.load(f)
        print(datas)
    return datas
