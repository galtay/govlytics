import os
import json
from py2neo import Graph, Node, Relationship
import legislators
import bills


currlegs = legislators.CurrentLegislators(legislators.LEGCURR_FNAME)


# get data on bills
#====================================================================
congress_num = 114
bill_type = 'hjres'
path = os.path.join(
    bills.DATA_PATH, str(congress_num), 'bills', bill_type)
all_bills = {}
for bill_dir in os.listdir(path):
    fname = os.path.join(path, bill_dir, 'data.json')
    with open(fname, 'r') as fp:
        bill_dict = json.load(fp)
        all_bills[bill_dict['bill_id']] = bills.Bill(bill_dict)


# add data to graph database
#====================================================================
username='neo4j'
password='neo'
graph = Graph("http://{}:{}@localhost:7474/db/data".format(
    username, password))
graph.delete_all()

nodes = {}
for legislator in currlegs:
    name = legislator.official_name
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


for bill_id, bill in all_bills.iteritems():

    short_title = bill.return_title(which='short')
    nodes[bill_id] = Node(
        'Bill', **{'bill_id':bill_id, 'short_title':short_title})

    if bill.sponsor['type'] == 'person':
        thomas_id = bill.sponsor['thomas_id']
        leg = currlegs.get_by_thomas(thomas_id)
        bioguide_id = leg.id_bioguide
        rel = Relationship(nodes[bioguide_id], "SPONSORED", nodes[bill_id])
        graph.create(rel)

    for cosponsor in bill.cosponsors:
        thomas_id = cosponsor['thomas_id']
        try:
            leg = currlegs.get_by_thomas(thomas_id)
        except KeyError:
            print 'cant find thomas ID {}'.format(thomas_id)
            continue
        bioguide_id = leg.id_bioguide
        rel = Relationship(nodes[bioguide_id], "COSPONSORED", nodes[bill_id])
        graph.create(rel)
