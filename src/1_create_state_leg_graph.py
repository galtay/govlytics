from py2neo import Graph, Node, Relationship
import legislators


def get_legislators():
    """Return legislators object."""
    return legislators.CurrentLegislators(legislators.LEGCURR_FNAME)


def map_legislators_to_state(currlegs):
    """Create graph with legislators connected to their states."""
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


def main():
    currlegs = get_legislators()
    map_legislators_to_state(currlegs)


if __name__ == '__main__':
    main()
