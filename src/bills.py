"""Module to handle bills data
from the GovTrack project (https://www.govtrack.us)
see https://github.com/unitedstates/congress
"""


import os
import json


PATH_HERE = os.path.dirname(os.path.abspath(__file__))
BASE_PATH = os.path.join(PATH_HERE, '..', 'data')
CON_PATH = os.path.join(BASE_PATH, 'congress')
DATA_PATH = os.path.join(CON_PATH, 'data')


class Bill(object):
    """Handles a bill object."""

    def __init__(self, bill_dict):
        """Initialize with json data read into a dictionary."""
        self._dict = bill_dict

        # set convenience attributes
        self.sponsor = self._dict['sponsor']
        self.cosponsors = self._dict['cosponsors']


    def return_title(self, which='official'):
        assert which in ['official', 'short', 'popular']
        return self._dict['{}_title'.format(which)]


if __name__ == '__main__':

    bill_fname = os.path.join(
        DATA_PATH, '114', 'bills', 'hr', 'hr3048', 'data.json')
    with open(bill_fname, 'r') as fp:
        bill_dict = json.load(fp)
    bill = Bill(bill_dict)
    print 'short title: {}'.format(bill.return_title(which='short'))
