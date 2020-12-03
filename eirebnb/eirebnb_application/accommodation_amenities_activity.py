from flask import render_template
from flask import Blueprint
from flask import Flask, Response, request,render_template
import json
from flask import url_for
import requests

bp = Blueprint("accommodation_amenities_activity", __name__, url_prefix="/accommodation-amenities-activity")

accommodation_amenities_activity_query = """
PREFIX HostURL:<http://www.semanticweb.org/ontologies/2020/10/Host>
PREFIX Activity: <http://www.semanticweb.org/ontologies/2020/10/Activity>
PREFIX owl:<http://www.w3.org/2002/07/owl#>
PREFIX rdfs:<http://www.w3.org/2007/01/rdf-schema#>
PREFIX xsd:<http://www.w3.org/2001/XMLSchema#>
SELECT DISTINCT ?amenities ?activity ?activityLocation {
  	?locationObject  <http://www.semanticweb.org/ontologies/2020/10/activityLocation> ?locationPredicate.
	?activityId <http://www.semanticweb.org/ontologies/2020/10/hasActivityType> <http://foo.example/ActivitiesTypes/Golf> .
	?activityId <http://www.semanticweb.org/ontologies/2020/10/activityName> ?activity .
    ?activityId <http://www.semanticweb.org/ontologies/2020/10/activityLocatedIn> ?activityLocation . 
    ?accomodationId <http://www.semanticweb.org/ontologies/2020/10/accommodationLocatedIn> ?activityLocation . 
    ?accomodationId <http://www.semanticweb.org/ontologies/2020/10/hasAmenities> ?amenitiesId . 
    ?amenitiesId <http://www.semanticweb.org/ontologies/2020/10/amenityName> ?amenities .
} ORDER BY ?activityLocation
"""

@bp.route("/", methods=["GET"])
def accommodation_amenities_activity():
    response = requests.post('http://localhost:3030/eirebnb/sparql',
        data={'query': accommodation_amenities_activity_query})
    query_results = []
    response_accommodation_amenities_activity = response.json()['results']['bindings']
    
    for i in response_accommodation_amenities_activity:
        query_results.append((i['amenities']['value'], i['activity']['value'], i['activityLocation']['value'].split("/")[-1].replace(">", "")))
    
    
    competency_question_title = "Competency Question 5: Accommodation Amenities Activity"
    competency_question = """What are the amenities offered in accomodations for someone that wishes to visit Golf activity?"""
    results_set_vars = ["Amenity", "Property Type", "Activity Location" ]
    return render_template(
        "competency_question.html", 
        results_set_vars = results_set_vars, 
        results_set=query_results,
        competency_question_title=competency_question_title,
        competency_question=competency_question,
        query = accommodation_amenities_activity_query
    )
