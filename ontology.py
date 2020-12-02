# import rdflib

# g = rdflib.Graph()
# g.parse("output.ttl", format="turtle")

# qres = g.query(
#     """
# #What room types are available where there are fishing activities?
# PREFIX HostURL:<http://www.semanticweb.org/ontologies/2020/10/Host>
# PREFIX Activity: <http://www.semanticweb.org/ontologies/2020/10/Activity>
# PREFIX owl:<http://www.w3.org/2002/07/owl#>
# PREFIX rdfs:<http://www.w3.org/2007/01/rdf-schema#>
# PREFIX xsd:<http://www.w3.org/2001/XMLSchema#>
# SELECT ?roomType ?activityLocation {
#   ?location  <http://www.semanticweb.org/ontologies/2020/10/activityLocation> ?activityLocation .
#   ?accomLocation <http://www.semanticweb.org/ontologies/2020/10/accommodationLocatedIn> ?accomodationLocation .
#   ?room <http://www.semanticweb.org/ontologies/2020/10/isRoomType> ?roomTypeId .
#   ?roomTypeId <http://www.semanticweb.org/ontologies/2020/10/roomType> ?roomType .
#   ?activityId <http://www.semanticweb.org/ontologies/2020/10/hasActivityType> <http://foo.example/ActivitiesTypes/Fishing> .
#   ?activityId <http://www.semanticweb.org/ontologies/2020/10/activityName> ?activity .
# } GROUP BY ?roomType ?activityLocation
# """)


# for row in qres:
#     print(row)


import requests
response = requests.post('http://localhost:3030/test10/sparql',
       data={'query': """
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
"""})
print(response.json())
