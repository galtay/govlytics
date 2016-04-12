from py2neo import Graph, Node, Relationship
import legislators
import votes

# get data on legislators
#====================================================================
curlegs = legislators.CurrentLegislators(legislators.LEGCURR_FNAME)
senators = curlegs.return_by_type('sen')
representatives = curlegs.return_by_type('rep')

# get data on votes
#====================================================================
votes_dict = votes.get_votes(114, 2016)


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
        nodes[leg.id_bioguide] = Node(
            term['type'], party, **{'name':name, 'type':term['type']})
        if state not in nodes.keys():
            nodes[state] = Node("State", name=state)
        rel = Relationship(nodes[leg.id_bioguide], "FROM", nodes[state])
        graph.create(rel)


for vote_dict in votes_dict.values():
    vote_id = vote_dict['vote_id']
    nodes[vote_id] = Node('Vote', **{'vote_id':vote_id})
    for vote_type, voters in vote_dict['votes'].iteritems():
        for voter in voters:
            try:
                rel = Relationship(
                    nodes[voter['id']], "VOTED", nodes[vote_id],
                    **{'type': vote_type})
                graph.create(rel)
            except KeyError:
                print 'skipping {} VOTED {} on {}'.format(
                    voter['id'], vote_type, vote_id)
