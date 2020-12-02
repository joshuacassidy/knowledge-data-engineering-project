from flask import render_template
from flask import Blueprint
from flask import Flask, Response, request,render_template
import json
import rdflib
from flask import url_for

bp = Blueprint("activity_date_availability", __name__, url_prefix="/activity-date-availability")

activity_date_availability_query = """
PREFIX HostURL:<http://www.semanticweb.org/ontologies/2020/10/Host>
PREFIX Activity: <http://www.semanticweb.org/ontologies/2020/10/Activity>
PREFIX owl:<http://www.w3.org/2002/07/owl#>
PREFIX rdfs:<http://www.w3.org/2007/01/rdf-schema#>
PREFIX xsd:<http://www.w3.org/2001/XMLSchema#>
SELECT DISTINCT ?accommodationId ?accomadationName ?accomodationURL ?activity ?locationPredicate {
	?locationObject  <http://www.semanticweb.org/ontologies/2020/10/activityLocation> ?locationPredicate.
	?availabilityDate <http://www.semanticweb.org/ontologies/2020/10/availabilityDate> "2021-07-18" .
	?availableListing <http://www.semanticweb.org/ontologies/2020/10/hasAccommodationAvailabilities> ?availabilityDate .
	?availableListing <http://www.semanticweb.org/ontologies/2020/10/accommodationName> ?accomadationName . 
	?availableListing <http://www.semanticweb.org/ontologies/2020/10/accommodationLocatedIn> ?accomadationLocation . 
	?availableListing <http://www.semanticweb.org/ontologies/2020/10/accommodationId> ?accommodationId . 
    ?availableListing <http://www.semanticweb.org/ontologies/2020/10/accommodationURL> ?accomodationURL .
	?activityId <http://www.semanticweb.org/ontologies/2020/10/hasActivityType>  ?activityType.
	?activityId <http://www.semanticweb.org/ontologies/2020/10/activityName> ?activity .
    ?activityId <http://www.semanticweb.org/ontologies/2020/10/activityLocatedIn> ?activityLocation . 
    FILTER(?locationPredicate = "Dublin" && ?activityLocation = <http://foo.example/Location/Dublin> && ?activityType = <http://foo.example/ActivitiesTypes/Fishing>)
}
"""

@bp.route("/", methods=["GET"])
def activity_date_availability():
    results_set = []
    import requests
    response = requests.post('http://localhost:3030/test_project/sparql',
        data={'query': activity_date_availability_query})
    query_results = []
    response_activity_date_availability = response.json()['results']['bindings']
    
    for i in response_activity_date_availability:
        query_results.append((i['accomadationName']['value'], i['accomodationURL']['value'], i['activity']['value'], i['locationPredicate']['value']))
    
    competency_question_title = "Competency Question 4: Activity Date Availability"
    competency_question = "Where can someone stay to go fishing next summer on 2021-01-18?"
    results_set_vars = ["Accomadation Name", "Accomodation URL", "Activity", "Location"]
    return render_template(
        "competency_question.html", 
        results_set_vars = results_set_vars, 
        results_set=query_results,
        competency_question_title=competency_question_title,
        competency_question=competency_question
    )
