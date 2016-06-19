"""
Communicate with neo4j using the REST API
"""

NEO4J_BASE_URI = 'http://localhost:7474'

import requests



class Neo4j_API(object):

    def __init__(self, base_uri=NEO4J_BASE_URI):

        # send GET to root URI
        self.base_uri = base_uri
        req = requests.get(base_uri)
        reqj = req.json()
        self.data_uri = reqj['data']
        self.management_uri = reqj['management']

        # send GET to data and management
        req = requests.get(self.data_uri)
        self.data_json = req.json()
        req = requests.get(self.management_uri)
        self.management_json = req.json()

        # set cypher end point
        self.cypher_uri = self.data_json['cypher']



if __name__ == '__main__':

    na = Neo4j_API()

    make_node_json = {
        "query" : "CREATE (n:Person { props } ) RETURN n",
        "params" : {
            "props" : {
                "position" : "Developer",
                "name" : "Michael",
                "awesome" : True,
                "children" : 3
            }
        }
    }

    req = requests.post(na.cypher_uri, json=make_node_json)
