from flask import render_template
from flask import Blueprint
from flask import Flask, Response, request,render_template
import json
from flask import url_for
import requests

bp = Blueprint("activities_rating_communication", __name__, url_prefix="/activities-rating-communication")

activities_rating_communication_query = """
PREFIX AccRating:<http://www.semanticweb.org/ontologies/2020/10/AccommodationRating>
PREFIX AccName: <http://www.semanticweb.org/ontologies/2020/10/Accomodation>
PREFIX Activity:<http://www.semanticweb.org/ontologies/2020/10/Activity>
PREFIX owl:<http://www.w3.org/2002/07/owl#>
PREFIX rdfs:<http://www.w3.org/2007/01/rdf-schema#>
PREFIX xsd:<http://www.w3.org/2001/XMLSchema#>
SELECT DISTINCT ?activities ?CommunicationRating {
    ?rating <http://www.semanticweb.org/ontologies/2020/10/accommodationRatingCommunication> ?CommunicationRating .    
    ?activityType <http://www.semanticweb.org/ontologies/2020/10/activityTypeName> ?activities . 
  FILTER (?CommunicationRating >= 9)
}
"""

@bp.route("/", methods=["GET"])
def activities_rating_communication():
    response = requests.post('http://localhost:3030/eirebnb/sparql',
        data={'query': activities_rating_communication_query})
    query_results = []
    response_activities_rating_communication = response.json()['results']['bindings']
    
    for i in response_activities_rating_communication:
        query_results.append((i['activities']['value'], i['CommunicationRating']['value']))

    competency_question_title = "Competency Question 6: Activities Rating Communication"
    competency_question = "What activities can you do that have an communication rating of 9?"
    results_set_vars = ["Activities", "Communication Rating", ]
    return render_template(
        "competency_question.html", 
        results_set_vars = results_set_vars, 
        results_set=query_results,
        competency_question_title=competency_question_title,
        competency_question=competency_question,
        query = activities_rating_communication_query
    )
