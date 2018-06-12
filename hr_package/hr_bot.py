import json
from hr_package import utils as UTILS
from flask import Flask, request, jsonify
from hr_package import text_analysis as TA

app = Flask(__name__)


@app.route("/initiate_chat", methods=["POST"])
def start_chat():
    message = request.json['message']
    #response = UTILS.get_dummy_response(message,'leave')
    response = TA.getresponseOfQuery(message)
    #scenario_id = response[0]['scenarioId']
    scenario_id = '1'
    file_name=response
    #file_name = response[0]['response']
    response = UTILS.return_scenario_response(scenario_id, file_name)
    return jsonify(response)


@app.route("/scenario_response", methods=["POST"])
def fetch_scenario_response():
    scen_id = request.json['scenarioId']
    file_name = request.json['fileName']
    response = UTILS.return_scenario_response(scen_id, file_name)
    return jsonify(response)


if __name__ == '__main__':
    app.run(debug=True,port='5002')
