from flask import Flask, Response, request,render_template
import json
import rdflib

app = Flask(__name__)

@app.route('/', methods=['GET'])
def index():
    results_set = []

    return render_template("index.html", results_set=results_set)

@app.route('/query', methods=['POST'])
def queryOntologyGET():
    results_set = []
    return render_template("index.html", results_set=results_set)

@app.route('/query', methods=['POST'])
def queryOntology():
    query = request.form.get('query')
    results_set = []
    try:
        g = rdflib.Graph()
        g.parse("output.ttl", format="turtle")
        qres = g.query(query)
        for row in qres:
            results_set.append((str(row[0]), str(row[1]), str(row[2])))
            # break
    except:
        pass
    return render_template("index.html", results_set=results_set)


if __name__ == '__main__':
    app.run(debug=True)