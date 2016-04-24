"""Map out bills, their sponsors, and co-sponsors.

Try this query
MATCH (ee:Democrat)-[rel1:SPONSORED]-(bb:Bill)-[rel2:COSPONSORED]-(aa:Republican) RETURN *
"""

import os
import json
import govlytics


def get_bills():

    congress_num = 114
    bill_type = 'hjres'
    path = os.path.join(
        govlytics.gov.data_utils.CONGRESS_DATA_PATH,
        str(congress_num), 'bills', bill_type)
    all_bills = {}
    for bill_dir in os.listdir(path):
        fname = os.path.join(path, bill_dir, 'data.json')
        with open(fname, 'r') as fp:
            bill_dict = json.load(fp)
        all_bills[bill_dict['bill_id']] = govlytics.gov.bills.Bill(bill_dict)
    return all_bills

def main():
    currlegs = govlytics.gov.legislators.CurrentLegislators()
    graph = govlytics.graph.ops.return_graph()
    all_bills = get_bills()
    govlytics.graph.ops.map_legislator_bill_sponsorship(
        graph, currlegs, all_bills)

if __name__ == '__main__':
    main()
