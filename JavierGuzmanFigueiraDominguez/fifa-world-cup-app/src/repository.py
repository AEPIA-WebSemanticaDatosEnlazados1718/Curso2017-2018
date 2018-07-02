from rdflib import Graph
import pandas as pd


class Repository:

    def __init__(self):
        pd.set_option('display.max_colwidth', -1)
        self.graph = None
        self.prefix = """
            PREFIX geo: <http://www.w3.org/2003/01/geo/wgs84_pos#>
            PREFIX schema: <http://schema.org/>
            PREFIX fwc: <http://linkeddata.fifawordcup.org/ontology/WordCup#>
            PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
            PREFIX owl: <http://www.w3.org/2002/07/owl#>
            PREFIX gn: <http://www.geonames.org/ontology#>
            PREFIX xsd: <http://www.w3.org/2001/XMLSchema#>
            PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
            PREFIX event: <http://purl.org/NET/c4dm/event.owl#>
            PREFIX sport: <http://www.bbc.co.uk/ontologies/sport/>
            PREFIX foaf: <http://xmlns.com/foaf/0.1/>
        """

    def load_graph(self):
        print('Loading data...')

        self.graph = Graph()
        self.graph.parse('../../data/target/world_cup.ttl', format='turtle')

        print('Data loaded')

    def get_info(self):
        query = """
            SELECT ?year ?winner ?place ?totalAttendance
            WHERE { 
                ?year fwc:isWinner ?winner .
                ?year event:place ?place .
                ?year fwc:totalAttendance ?totalAttendance .
            }
            ORDER BY ASC(?year)
        """
        result = self.graph.query(self.prefix + query)

        return pd.DataFrame(result.bindings)

    def get_info_by_year(self, year):
        query = """
            SELECT ?match ?time ?city ?attendance
            WHERE { 
                ?year sport:hasMatch ?match .
                ?match event:time ?time .
                ?match event:place ?stadium .
                ?stadium foaf:based_near ?city .
                ?match fwc:totalAttendance ?attendance .
                FILTER (?year = <http://linkeddata.fifawordcup.org/resources/Year/""" + str(year) + """>)
            } 
            ORDER BY ASC(?time)
        """
        result = self.graph.query(self.prefix + query)

        return pd.DataFrame(result.bindings)

    def get_team_ids(self):
        query = """
            SELECT DISTINCT ?team ?code
            WHERE {
                { 
                    ?match sport:homeCompetitor ?team . 
                    ?team gn:countryCode ?code .
                } 
                    UNION
                { 
                    ?match sport:awayCompetitor ?team . 
                    ?team gn:countryCode ?code .
                }
            }
            ORDER BY ASC(?team)
        """
        result = self.graph.query(self.prefix + query)

        return pd.DataFrame(result.bindings)

    def get_goals_by_team(self):
        query = """
            SELECT ?code (SUM(?goals) AS ?sum)
            WHERE {
                {
                    ?match sport:homeCompetitor ?team .
                    ?team gn:countryCode ?code .
                    ?match fwc:homeGoals ?goals .
                }
                    UNION
                {
                    ?match sport:awayCompetitor ?team .
                    ?team gn:countryCode ?code .
                    ?match fwc:awayGoals ?goals .
                }
            }
            GROUP BY ?team
            ORDER BY DESC(?sum)
        """
        result = self.graph.query(self.prefix + query)

        return pd.DataFrame(result.bindings)

    def get_matches_by_player(self):
        query = """
            SELECT ?playerName (COUNT(?playerName) AS ?count)
            WHERE {
                ?player fwc:fullName ?playerName
            }
            GROUP BY ?playerName
            ORDER BY DESC(?count)
            LIMIT 50
        """
        result = self.graph.query(self.prefix + query)

        return pd.DataFrame(result.bindings)
