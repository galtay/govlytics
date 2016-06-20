"""Takes data and inputs it into neo4j database
"""

from __future__ import print_function
from py2neo import Graph, Node, Relationship


def return_graph(username='neo4j', password='neo4jgov'):
#    graph = Graph("http://{}:{}@localhost:7474/db/data".format(
#        username, password))
    graph = Graph("http://localhost:7474/db/data".format(
        username, password))
    return graph

def delete(graph):
    graph.delete_all()

def map_legislators_to_state(graph, legs):
    """Create graph with legislators connected to their states."""
    delete(graph)
    nodes = {}
    for leg in legs:
        if leg.official_name:
            name = leg.official_name
        else:
            name = '{} {}'.format(leg.first_name, leg.last_name)
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


def map_legislator_bill_sponsorship(graph, legs, bills):
    """Create graph with bills connected to the legislators who sponsored
    and co-sponsored them."""
    delete(graph)

    nodes = {}
    for legislator in legs:
        if legislator.official_name:
            name = legislator.official_name
        else:
            name = '{} {}'.format(legislator.first_name, legislator.last_name)
        term = legislator.most_recent_term
        state = term['state']
        party = term['party']
        nodes[legislator.id_bioguide] = Node(
            term['type'], party, **{'name':name, 'type':term['type']})
        if state not in nodes.keys():
            nodes[state] = Node("State", **{'name':state})
        rel = Relationship(
            nodes[legislator.id_bioguide], "FROM", nodes[state])
        graph.create(rel)


    for bill_id, bill in bills.iteritems():

        node_props = {
            'bill_id': bill_id,
            'short_title': bill.return_title(which='short'),
            'official_title': bill.return_title(which='official'),
        }
        nodes[bill_id] = Node('Bill', **node_props)

        if bill.sponsor['type'] == 'person':
            thomas_id = bill.sponsor['thomas_id']
            leg = legs.get_by_thomas(thomas_id)
            bioguide_id = leg.id_bioguide
            rel = Relationship(nodes[bioguide_id], "SPONSORED", nodes[bill_id])
            graph.create(rel)

        for cosponsor in bill.cosponsors:
            thomas_id = cosponsor['thomas_id']
            try:
                leg = legs.get_by_thomas(thomas_id)
            except KeyError:
                print('cant find thomas ID {}'.format(thomas_id))
                continue
            bioguide_id = leg.id_bioguide
            rel = Relationship(nodes[bioguide_id], "COSPONSORED", nodes[bill_id])
            graph.create(rel)
