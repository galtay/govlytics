from py2neo import Graph, Node, Relationship
import legislators


# get data on legislators
#====================================================================
curlegs = legislators.CurrentLegislators(legislators.LEGCURR_FNAME)
senators = curlegs.return_by_type('sen')
representatives = curlegs.return_by_type('rep')



# add it to graph database
#====================================================================
username='neo4j'
password='neo'
graph = Graph("http://{}:{}@localhost:7474/db/data".format(
    username, password))
graph.delete_all()

nodes = {}

for senator in senators:
    state = senator.return_most_recent_state()
    name = senator.return_official_name()
    nodes[name] = Node("Senator", name=name)
    if state not in nodes.keys():
        nodes[state] = Node("State", name=state)
    rel = Relationship(nodes[name], "FROM", nodes[state])
    graph.create(rel)

for representative in representatives:
    state = representative.return_most_recent_state()
    name = representative.return_official_name()
    nodes[name] = Node("Representative", name=name)
    if state not in nodes.keys():
        nodes[state] = Node("State", name=state)
    rel = Relationship(nodes[name], "FROM", nodes[state])
    graph.create(rel)
