from flask import render_template
from flask import Blueprint
from flask import Flask, Response, request,render_template
import json
from flask import url_for
import requests

bp = Blueprint("activity_type_price", __name__, url_prefix="/activity-type-price")

activity_type_price_query = """
PREFIX HostURL:<http://www.semanticweb.org/ontologies/2020/10/Host>
PREFIX Activity: <http://www.semanticweb.org/ontologies/2020/10/Activity>
PREFIX owl:<http://www.w3.org/2002/07/owl#>
PREFIX rdfs:<http://www.w3.org/2007/01/rdf-schema#>
PREFIX xsd:<http://www.w3.org/2001/XMLSchema#>
SELECT DISTINCT ?accomadationName ?availabilityDate ?activity {
    ?activityId <http://www.semanticweb.org/ontologies/2020/10/hasActivityType> <http://foo.example/ActivitiesTypes/Fishing> .
    ?activityId <http://www.semanticweb.org/ontologies/2020/10/activityName> ?activity .
    ?activityId <http://www.semanticweb.org/ontologies/2020/10/activityLocatedIn> ?activityLocation .
    ?listingId <http://www.semanticweb.org/ontologies/2020/10/accommodationLocatedIn> ?activityLocation . 
    ?listingId <http://www.semanticweb.org/ontologies/2020/10/hasAccommodationAvailabilities> ?availability .
    ?listingId <http://www.semanticweb.org/ontologies/2020/10/accommodationName> ?accomadationName .
    ?availability <http://www.semanticweb.org/ontologies/2020/10/availabilityDate> ?availabilityDate .
    ?availability <http://www.semanticweb.org/ontologies/2020/10/availabilityPrice> ?price .
    FILTER(?price <= 250.00)
} order by ?availabilityDate
"""

@bp.route("/", methods=["GET"])
def activity_type_price():
    response = requests.post('http://localhost:3030/eirebnb/sparql',
        data={'query': activity_type_price_query})
    query_results = []
    response_activity_type_price = response.json()['results']['bindings']
    
    for i in response_activity_type_price:
        query_results.append((i['accomadationName']['value'], i['availabilityDate']['value'], i['activity']['value']))
    
    competency_question_title = "Competency Question 8: Activity Type Price"
    competency_question = "Where can someone stay to go on a fishing holiday for under 250 euro?"
    results_set_vars = ["Accomadation Name", "Availability Date", "Activity"]
    return render_template(
        "competency_question.html", 
        results_set_vars = results_set_vars, 
        results_set=query_results,
        competency_question_title=competency_question_title,
        competency_question=competency_question,
        query = activity_type_price_query
    )

