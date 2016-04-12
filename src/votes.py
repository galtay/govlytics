"""Module to handle voting records
from the GovTrack project (https://www.govtrack.us)
see https://github.com/unitedstates/congress
"""


import os
import json


PATH_HERE = os.path.dirname(os.path.abspath(__file__))
BASE_PATH = os.path.join(PATH_HERE, '..', 'data')
CON_PATH = os.path.join(BASE_PATH, 'congress')
DATA_PATH = os.path.join(CON_PATH, 'data')


def get_votes(congress, session):
    """Fetches voting data."""
    path = os.path.join(DATA_PATH, str(congress), 'votes', str(session))
    votes_dict = {}
    for vote in os.listdir(path):
        fname = os.path.join(path, vote, 'data.json')
        with open(fname, 'r') as fp:
            votes_dict[vote] = json.load(fp)
    return votes_dict

if __name__ == '__main__':

    votes_dict = get_votes('114', '2016')
