from flask import render_template
from flask import Blueprint
from flask import Flask, Response, request,render_template
import json
import rdflib
from flask import url_for

bp = Blueprint("property_type_activities", __name__, url_prefix="/property-type-activities")

property_types_activities_query = """
PREFIX MostActivity:<http://www.semanticweb.org/ontologies/2020/10/Activity>
PREFIX County:  <http://www.semanticweb.org/ontologies/2020/10/Location>
PREFIX owl:<http://www.w3.org/2002/07/owl#>
PREFIX rdfs:<http://www.w3.org/2007/01/rdf-schema#>
PREFIX xsd:<http://www.w3.org/2001/XMLSchema#>
SELECT ?activityLocation  WHERE{
?activityType <http://www.semanticweb.org/ontologies/2020/10/activityTypeName> ?Activities .
?location  <http://www.semanticweb.org/ontologies/2020/10/activityLocation> ?activityLocation .
?name <http://www.semanticweb.org/ontologies/2020/10/propertyType> ?propertyType .
FILTER (?Activities = "Fishing" && ?propertyType = "Entire condominium") 
} GROUP BY ?activityLocation
"""

@bp.route("/", methods=["GET"])
def property_type_activities():
    results_set = []
    import requests
    response = requests.post('http://localhost:3030/test_project/sparql',
        data={'query': property_types_activities_query})
    query_results = []
    for i in response.json()['results']['bindings']:
        query_results.append([i['activityLocation']['value']])

    competency_question_title = "Competency Question 2: Property Type Activities"
    competency_question = "What counties can you go fishing in and stay in a apartment?"
    results_set_vars = ["Location Name"]
    return render_template(
        "competency_question.html", 
        results_set_vars = results_set_vars, 
        results_set=query_results,
        competency_question_title=competency_question_title,
        competency_question=competency_question
    )
