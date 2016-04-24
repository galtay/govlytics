"""Takes data and inputs it into neo4j database
"""

from py2neo import Graph, Node, Relationship


def return_graph(username='neo4j', password='neo'):
    graph = Graph("http://{}:{}@localhost:7474/db/data".format(
        username, password))
    return graph

def delete(graph):
    graph.delete_all()

def map_legislators_to_state(graph, legs):
    """Create graph with legislators connected to their states."""
    delete(graph)
    nodes = {}
    for leg in legs:
        name = leg.official_name
        term = leg.most_recent_term
        state = term['state']
        party = term['party']
        nodes[leg.id_bioguide] = Node(
            term['type'], party, **{'name':name, 'type':term['type']})
        if state not in nodes.keys():
            nodes[state] = Node("State", **{'name':state})
        rel = Relationship(
            nodes[leg.id_bioguide], "FROM", nodes[state])
        graph.create(rel)
