"""Module to handle legislator data (current and historical)
from the GovTrack project (https://www.govtrack.us)
see https://github.com/unitedstates/congress-legislators
"""


import os
import pyaml


PATH_HERE = os.path.dirname(os.path.abspath(__file__))
BASE_PATH = os.path.join(PATH_HERE, '..', 'data')
CONLEG_PATH = os.path.join(BASE_PATH, 'congress-legislators')
LEGCURR_FNAME = os.path.join(CONLEG_PATH, 'legislators-current.yaml')


class Legislator(object):
    """Handles the dictionary for a single legislator."""

    def __init__(self, legislator_dict):
        self._legislator_dict = legislator_dict
        self.id_bioguide = self._legislator_dict['id']['bioguide']

    def return_most_recent_term(self):
        return self._legislator_dict['terms'][-1]

    def return_most_recent_state(self):
        return self.return_most_recent_term()['state']

    def return_official_name(self):
        return self._legislator_dict['name']['official_full']


class CurrentLegislators(object):
    """Handles a collection of legislators."""

    def __init__(self, yaml_fname):
        with open(yaml_fname, 'r') as fp:
            leg_dicts = pyaml.yaml.load(fp)
        self.legs = [Legislator(leg_dict) for leg_dict in leg_dicts]

    def return_by_type(self, legtype):
        assert(legtype in ['sen', 'rep'])
        legislators = []
        for leg in self.legs:
            mrt = leg.return_most_recent_term()
            if mrt['type'] == legtype:
                legislators.append(leg)
        return legislators


if __name__ == '__main__':

    curlegs = CurrentLegislators(LEGCURR_FNAME)
    senators = curlegs.return_by_type('sen')
    representatives = curlegs.return_by_type('rep')

    for senator in senators:
        print (
            senator.return_most_recent_state(),
            senator.return_official_name(),
        )
