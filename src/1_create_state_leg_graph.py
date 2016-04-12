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
for legislators in [senators, representatives]:
    for leg in legislators:
        name = leg.return_official_name()
        term = leg.return_most_recent_term()
        state = term['state']
        party = term['party']
        nodes[name] = Node(party, **{'name':name, 'type':term['type']})
        if state not in nodes.keys():
            nodes[state] = Node("State", name=state)
        rel = Relationship(nodes[name], "FROM", nodes[state])
        graph.create(rel)
