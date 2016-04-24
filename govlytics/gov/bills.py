"""Module to handle bills data
from the GovTrack project (https://www.govtrack.us)
see https://github.com/unitedstates/congress
"""


import os
import json
import logging
from . import data_utils


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


def main():
    bill_fname = os.path.join(
        data_utils.CONGRESS_DATA_PATH,
        '114', 'bills', 'hr', 'hr3048', 'data.json')
    with open(bill_fname, 'r') as fp:
        bill_dict = json.load(fp)
    bill = Bill(bill_dict)
    print 'short title: {}'.format(bill.return_title(which='short'))


if __name__ == '__main__':
    main()
