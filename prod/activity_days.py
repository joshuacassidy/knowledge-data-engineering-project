# amenities
from flask import render_template
from flask import Blueprint
from flask import Flask, Response, request,render_template
import json
import rdflib
from flask import url_for

bp = Blueprint("activity_days", __name__, url_prefix="/activity-days")

activity_days_query = """
PREFIX HostURL:<http://www.semanticweb.org/ontologies/2020/10/Host>
PREFIX Activity: <http://www.semanticweb.org/ontologies/2020/10/Activity>
PREFIX owl:<http://www.w3.org/2002/07/owl#>
PREFIX rdfs:<http://www.w3.org/2007/01/rdf-schema#>
PREFIX xsd:<http://www.w3.org/2001/XMLSchema#>
SELECT DISTINCT ?accomadationName ?locationName ?activity ?availabilityDate ?availabilityMin{
    ?activityId <http://www.semanticweb.org/ontologies/2020/10/hasActivityType> <http://foo.example/ActivitiesTypes/Fishing> .
    ?activityId <http://www.semanticweb.org/ontologies/2020/10/activityName> ?activity .
    ?activityId <http://www.semanticweb.org/ontologies/2020/10/activityLocatedIn> ?activityLocation .
    ?locationId <http://www.semanticweb.org/ontologies/2020/10/partOfRegion>?activityLocation .
    ?locationId <http://www.semanticweb.org/ontologies/2020/10/countyName> ?locationName .
    ?listingId <http://www.semanticweb.org/ontologies/2020/10/accommodationLocatedIn> ?activityLocation . 
    ?listingId <http://www.semanticweb.org/ontologies/2020/10/hasAccommodationAvailabilities> ?availability .
    ?availability <http://www.semanticweb.org/ontologies/2020/10/availabilityDate> ?availabilityDate .
    ?listingId <http://www.semanticweb.org/ontologies/2020/10/accommodationName> ?accomadationName .
    ?availability <http://www.semanticweb.org/ontologies/2020/10/availabilityMin> ?availabilityMin .
    FILTER(?availabilityMin <= 3)
}
"""

@bp.route("/", methods=["GET"])
def activity_days():
    results_set = []
    import requests
    response = requests.post('http://localhost:3030/test_project/sparql',
        data={'query': activity_days_query})
    query_results = []
    response_activity_days = response.json()['results']['bindings']
    
    for i in response_activity_days:
        query_results.append([
            i['accomadationName']['value'], 
            i['locationName']['value'], 
            i['activity']['value'], 
            i['availabilityDate']['value'], 
            i['availabilityMin']['value'], 
        ])
    
    competency_question_title = "Competency Question 10: Activity Days"
    competency_question = "Where can someone go on a fishing holiday for atleast 3 nights?"
    results_set_vars = ["Accomadation Name", "Location Name", "Activity", "Availability Date", "Days Available"]
    return render_template(
        "competency_question.html", 
        results_set_vars = results_set_vars, 
        results_set=query_results,
        competency_question_title=competency_question_title,
        competency_question=competency_question
    )
