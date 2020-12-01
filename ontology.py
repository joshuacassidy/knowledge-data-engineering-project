import rdflib

g = rdflib.Graph()
g.parse("output.ttl", format="turtle")

qres = g.query(
    """SELECT DISTINCT * WHERE {
  ?s ?p ?o
}
LIMIT 10
""")


for row in qres:
    print(row)
