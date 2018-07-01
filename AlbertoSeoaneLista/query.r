library(SPARQL) # SPARQL querying package
library(ggplot2)

url<- "museosMurcia.ttl"

prefix <- c("owl","<http://www.w3.org/2002/07/owl#>",
            "rdf","<http://www.w3.org/1999/02/22-rdf-syntax-ns#>",
            "rdfx","<http://www.w3.org/2001/rdf-schema#>",
            "vcard","<http://www.w3.org/2006/vcard/ns#>"
)
query<-'SELECT ?direccion
WHERE {
?museo vcard:hasAddress ?direccion .
?museo rdfs:label ?nombre .	
FILTER(str(?nombre) = "Aquarium") .
}'
qd <- SPARQL(url,query)
df <- qd$results

query<-'SELECT ?municipio
WHERE {
?museo vcard:hasRegion ?municipio .
?museo rdfs:label ?nombre .	
FILTER(str(?nombre) = "Aquarium") .
}'
qd <- SPARQL(url,query)
df <- qd$results


query<-'SELECT *
WHERE {

OPTIONAL{?museo vcard:hasAddress ?direccion} .
OPTIONAL{?museo vcard:hasRegion ?municipio} .
OPTIONAL{?museo vcard:hasLocality ?pedania} .
OPTIONAL{?museo vcard:hasEmail ?email} .
OPTIONAL{?museo vcard:hasUrl ?web} .
OPTIONAL{?museo vcard:hasTelephone ?telefono} .
OPTIONAL{?museo rdfs:label ?nombre} .	
FILTER(str(?nombre) = "ARQUA Museo Nacional de Arqueología Subacuática") .
}'
qd <- SPARQL(url,query)
df <- qd$results
