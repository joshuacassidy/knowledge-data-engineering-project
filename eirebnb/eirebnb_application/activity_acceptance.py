from flask import render_template
from flask import Blueprint
from flask import Flask, Response, request,render_template
import json
from flask import url_for
import requests

bp = Blueprint("activity_acceptance", __name__, url_prefix="/activity-acceptance")

activity_acceptance_query = """
PREFIX HostURL:<http://www.semanticweb.org/ontologies/2020/10/Host>
PREFIX Activity: <http://www.semanticweb.org/ontologies/2020/10/Activity>
PREFIX owl:<http://www.w3.org/2002/07/owl#>
PREFIX rdfs:<http://www.w3.org/2007/01/rdf-schema#>
PREFIX xsd:<http://www.w3.org/2001/XMLSchema#>
SELECT DISTINCT ?hostName ?acceptanceRate ?roomType ?activityLocation  {
    ?activityId <http://www.semanticweb.org/ontologies/2020/10/activityName> "Ardgillan Demesne" .
    ?activityId  <http://www.semanticweb.org/ontologies/2020/10/activityLocatedIn> ?activityLocation .
    ?accomodationId <http://www.semanticweb.org/ontologies/2020/10/accommodationLocatedIn> ?activityLocation .
    ?accomodationId <http://www.semanticweb.org/ontologies/2020/10/isRoomType> ?roomTypeId .
    ?roomTypeId <http://www.semanticweb.org/ontologies/2020/10/roomType> ?roomType .
    ?accomodationId <http://www.semanticweb.org/ontologies/2020/10/accommodationOwnedBy> ?hostId .
    ?hostId <http://www.semanticweb.org/ontologies/2020/10/hostAcceptanceRate> ?acceptanceRate .
    ?hostId <http://www.semanticweb.org/ontologies/2020/10/hostName> ?hostName
    FILTER (?acceptanceRate >= 70)  
}
"""

@bp.route("/", methods=["GET"])
def activity_acceptance():
    response = requests.post('http://localhost:3030/eirebnb/sparql',
        data={'query': activity_acceptance_query})
    query_results = []
    response_activity_acceptance = response.json()['results']['bindings']
    
    for i in response_activity_acceptance:
        query_results.append([
            i['hostName']['value'], 
            i['acceptanceRate']['value'], 
            i['roomType']['value'], 
            i['activityLocation']['value'], 
        ])

    competency_question_title = "Competency Question 9: Activity Acceptance"
    competency_question = """What are the accommodations are available dates to visit "Ardgillan Demesne" where the host has an acceptance rate of 7?"""
    
    results_set_vars = ["Host Name", "Acceptance Rate", "Room Type", "Activity Location"]
    return render_template(
        "competency_question.html", 
        results_set_vars = results_set_vars, 
        results_set=query_results,
        competency_question_title=competency_question_title,
        competency_question=competency_question,
        query = activity_acceptance_query
    )
