from flask import render_template
from flask import Blueprint
from flask import Flask, Response, request,render_template
import json
import rdflib
from flask import url_for

bp = Blueprint("accommodation_activities_beds", __name__, url_prefix="/accommodation-activities-beds")

accommodation_activities_beds_query = """
PREFIX MostActivity:<http://www.semanticweb.org/ontologies/2020/10/Activity>
PREFIX County:  <http://www.semanticweb.org/ontologies/2020/10/Location>
PREFIX Accommodation: <http://www.semanticweb.org/ontologies/2020/10/Accomedation>
PREFIX owl:<http://www.w3.org/2002/07/owl#>
PREFIX rdfs:<http://www.w3.org/2007/01/rdf-schema#>
PREFIX xsd:<http://www.w3.org/2001/XMLSchema#>
SELECT ?activityLocation ?propertyType WHERE{
	?activityType <http://www.semanticweb.org/ontologies/2020/10/activityTypeName> ?Activities .
	?location  <http://www.semanticweb.org/ontologies/2020/10/activityLocation> ?activityLocation .
	?name <http://www.semanticweb.org/ontologies/2020/10/propertyType> ?propertyType .
	?type <http://www.semanticweb.org/ontologies/2020/10/accommodationBeds> ?Beds
	FILTER (?Activities = "Fishing" && ?Beds >= 3)
} GROUP BY ?activityLocation ?propertyType ORDER BY ?activityLocation
"""

@bp.route("/", methods=["GET"])
def accommodation_activities_beds():
    results_set = []
    import requests
    response = requests.post('http://localhost:3030/test_project/sparql',
        data={'query': accommodation_activities_beds_query})
    query_results = []
    response_accommodation_activities_beds = response.json()['results']['bindings']
    
    for i in response_accommodation_activities_beds:
        query_results.append([i['propertyType']['value'], i['activityLocation']['value']])

    competency_question_title = "Competency Question 3: Accommodation Activities Beds"
    competency_question = """What accomodations can you stay in to go fishing that have more than 3 beds?"""
    results_set_vars = ["Activity Location", "Rroperty Type"]
    return render_template(
        "competency_question.html", 
        results_set_vars = results_set_vars, 
        results_set=query_results,
        competency_question_title=competency_question_title,
        competency_question=competency_question
    )
