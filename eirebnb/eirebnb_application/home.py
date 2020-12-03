from flask import render_template
from flask import Blueprint
from flask import Flask, Response, request,render_template
import json
from flask import url_for
import requests

bp = Blueprint("index", __name__, url_prefix="/")

@bp.route("/", methods=["GET"])
def index():
    results_set = []

    return render_template("index.html", results_set=results_set)

@bp.route('/query', methods=['GET'])
def queryOntologyGET():
    results_set = []
    return render_template("index.html", results_set=results_set)

@bp.route('/query', methods=['POST'])
def queryOntology():
    query = request.form.get('query')
    
    results_set = []
    response = requests.post('http://localhost:3030/eirebnb/sparql',
        data={'query': query})
    query_results = []
    response_json = response.json()


    response_activitiy_host_head = response_json['head']['vars']
    response_activitiy_host = []
    for i in response_json['results']['bindings']:
        record = []
        for k, v in i.items():
            record.append(v['value'])
        response_activitiy_host.append(record)
    
    return render_template("index.html", results_set_vars=response_activitiy_host_head, results_set=response_activitiy_host)



