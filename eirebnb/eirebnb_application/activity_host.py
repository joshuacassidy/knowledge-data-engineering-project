import requests
from flask import render_template
from flask import Blueprint
from flask import Flask, Response, request,render_template
import json
from flask import url_for

bp = Blueprint("activitiy_host", __name__, url_prefix="/activity-host")

activitiy_host_query = """
PREFIX HostURL:<http://www.semanticweb.org/ontologies/2020/10/Host>
PREFIX Activity: <http://www.semanticweb.org/ontologies/2020/10/Activity>
PREFIX owl:<http://www.w3.org/2002/07/owl#>
PREFIX rdfs:<http://www.w3.org/2007/01/rdf-schema#>
PREFIX xsd:<http://www.w3.org/2001/XMLSchema#>
SELECT DISTINCT ?accomadationName ?hostName ?activity ?accommodationLocation {
	?activityId <http://www.semanticweb.org/ontologies/2020/10/hasActivityType> <http://foo.example/ActivitiesTypes/Shopping> .
    <http://foo.example/ActivitiesTypes/Shopping> <http://www.semanticweb.org/ontologies/2020/10/activityTypeName> ?activity .
    ?activityId <http://www.semanticweb.org/ontologies/2020/10/activityLocatedIn> ?activityLocation . 
    ?accomodationId <http://www.semanticweb.org/ontologies/2020/10/accommodationLocatedIn> ?accommodationLocation . 
    ?accomodationId <http://www.semanticweb.org/ontologies/2020/10/accommodationName> ?accomadationName . 
    ?hostId <http://www.semanticweb.org/ontologies/2020/10/ownsAccommodation> ?accomodationId .
    ?hostId <http://www.semanticweb.org/ontologies/2020/10/hostId> "234243" .
    ?hostId <http://www.semanticweb.org/ontologies/2020/10/hostName> ?hostName
} GROUP BY ?accomadationName ?hostName ?activity ?accommodationLocation
"""

@bp.route("/", methods=["GET"])
def activitiy_host():
    response = requests.post('http://localhost:3030/eirebnb/sparql',
        data={'query': activitiy_host_query})
    query_results = []
    response_activitiy_host = response.json()['results']['bindings']
    
    for i in response_activitiy_host:
        query_results.append((i['accomadationName']['value'], i['hostName']['value'], i['accommodationLocation']['value'].split("/")[-1].replace(">", ""), i['activity']['value']))
    
    competency_question_title = "Competency Question 7: Activity Host"
    competency_question = "What properties does host 234243 have in the same county as the Shopping Activity?"
    results_set_vars = ["Accomadation Name", "Host Name", "Location", "Activity"]
    return render_template(
        "competency_question.html", 
        results_set_vars = results_set_vars, 
        results_set=query_results,
        competency_question_title=competency_question_title,
        competency_question=competency_question,
        query = activitiy_host_query
    )
