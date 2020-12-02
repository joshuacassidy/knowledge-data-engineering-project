from flask import render_template
from flask import Blueprint
from flask import Flask, Response, request,render_template
import json
import rdflib
from flask import url_for

bp = Blueprint("room_type_activities", __name__, url_prefix="/room-type-activities")

room_type_activities_query = """
PREFIX HostURL:<http://www.semanticweb.org/ontologies/2020/10/Host>
PREFIX Activity: <http://www.semanticweb.org/ontologies/2020/10/Activity>
PREFIX owl:<http://www.w3.org/2002/07/owl#>
PREFIX rdfs:<http://www.w3.org/2007/01/rdf-schema#>
PREFIX xsd:<http://www.w3.org/2001/XMLSchema#>
SELECT ?roomType ?activityLocation {
?location  <http://www.semanticweb.org/ontologies/2020/10/activityLocation> ?activityLocation .
?accomLocation <http://www.semanticweb.org/ontologies/2020/10/accommodationLocatedIn> ?accomodationLocation .
?room <http://www.semanticweb.org/ontologies/2020/10/isRoomType> ?roomTypeId .
?roomTypeId <http://www.semanticweb.org/ontologies/2020/10/roomType> ?roomType .
?activityId <http://www.semanticweb.org/ontologies/2020/10/hasActivityType> <http://foo.example/ActivitiesTypes/Fishing> .
?activityId <http://www.semanticweb.org/ontologies/2020/10/activityName> ?activity .
} GROUP BY ?roomType ?activityLocation
"""

@bp.route("/", methods=["GET"])
def room_type_activities():
    results_set = []
    import requests
    response = requests.post('http://localhost:3030/test_project/sparql',
        data={'query': room_type_activities_query})
    query_results = []
    for i in response.json()['results']['bindings']:
        query_results.append((i['roomType']['value'], i['activityLocation']['value']))

    competency_question_title = "Competency Question 1: Room Type Activities"
    competency_question = "What room types are available where there are fishing activities?"
    results_set_vars = ["Room Type", "Activity Location"]
    return render_template(
        "competency_question.html", 
        results_set_vars = results_set_vars, 
        results_set=query_results,
        competency_question_title=competency_question_title,
        competency_question=competency_question
    )


@bp.route("/accommodations", methods=["GET"])
def room_type_activities_accommodations():
    results_set = []
    import requests
    response = requests.post('http://localhost:3030/test_project/sparql',
        data={'query': room_type_activities_query})
    query_results = []
    for i in response.json()['results']['bindings']:
        query_results.append((i['roomType']['value'], i['activityLocation']['value']))

    return render_template("room_type_activities/index.html", results_set=query_results)

