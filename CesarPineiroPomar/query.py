import rdflib, sys
from rdflib import Graph
from rdflib.plugins import sparql

graph = Graph()
graph.load("alojamientoshoteleros.ttl", format='turtle')

prefix = """
PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
PREFIX owl: <http://www.w3.org/2002/07/owl#>
PREFIX xsd: <http://www.w3.org/2001/XMLSchema>
PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
PREFIX vcard: <http://www.w3.org/2006/vcard/ns#>
PREFIX db: <http://dbpedia.org/ontology/>
"""
try:
	while True:
		try:
			print(prefix)
			print("SparQL>", end="", flush=True)
			query = prefix + "\n".join(sys.stdin.readlines())
			for i, result in enumerate(graph.query(query)):
				print (str(i + 1)+":\t"+str(', '.join(map(lambda x : x or "",result))))
		except Exception as ex:
			print(ex)
except:
	print("\nAborting...")
