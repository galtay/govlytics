"""Module to handle legislator data (current and historical)
from the GovTrack project (https://www.govtrack.us)
see https://github.com/unitedstates/congress-legislators
"""


import os
import yaml
import logging
from . import data_utils


def read_yaml_file(fpath):
    """Read YAML into dictionary."""
    with open(fpath, 'r') as fp:
        yaml_dict = yaml.load(fp.read(), Loader=yaml.CLoader)
    return yaml_dict


class Legislator(object):
    """Handles data for a single legislator."""

    def __init__(self, legislator_dict):
        self._dict = legislator_dict

        # set convenience attributes
        self.id_bioguide = self._dict['id']['bioguide']
        self.id_thomas = self._dict['id']['thomas']
        self.most_recent_term = self._dict['terms'][-1]
        self.most_recent_state = self.most_recent_term['state']
        self.official_name = self._dict['name']['official_full']


class CurrentLegislators(object):
    """Handles a collection of legislators."""

    def __init__(
            self,
            yaml_fname=data_utils.CONGRESS_LEGISLATORS_CURRENT_FNAME):

        # check if data exists and get it if it doesn't
        if not os.path.isfile(yaml_fname):
            logging.info(
                'current legislators file not found.'.format(yaml_fname))
            data_utils._get_congress_legislators()

        # read legislator file
        leg_dicts = read_yaml_file(yaml_fname)

        # create a list of legislator objects
        self.legislators = [Legislator(leg_dict) for leg_dict in leg_dicts]

        # store senators and representatives
        self.senators = []
        self.representatives = []
        for leg in self:
            term_type = leg.most_recent_term['type']
            if term_type == 'sen':
                self.senators.append(leg)
            elif term_type == 'rep':
                self.representatives.append(leg)
            else:
                print 'unrecognized term type {}'.format(term_type)
                sys.exit(1)

        # store democrates, republicans, and independents
        self.democrats = []
        self.republicans = []
        self.independents = []
        for leg in self:
            party = leg.most_recent_term['party']
            if party == 'Democrat':
                self.democrats.append(leg)
            elif party == 'Republican':
                self.republicans.append(leg)
            elif party == 'Independent':
                self.independents.append(leg)
            else:
                print 'unrecognized party {}'.format(party)
                sys.exit(1)

        # index by bioguide ID
        self._indx_bioguide = {}
        for i, leg in enumerate(self):
            self._indx_bioguide[leg.id_bioguide] = i

        # index by thomas ID
        self._indx_thomas = {}
        for i, leg in enumerate(self):
            self._indx_thomas[leg.id_thomas] = i

    def __iter__(self):
        """Allow iteration over list of legislators."""
        indx = 0
        while indx < len(self.legislators):
            yield self.legislators[indx]
            indx += 1

    def get_by_thomas(self, id_thomas):
        indx = self._indx_thomas[id_thomas]
        return self.legislators[indx]

    def get_by_bioduide(self, id_bioguid):
        indx = self._indx_bioguide[id_bioguide]
        return self.legislators[indx]

if __name__ == '__main__':

    currlegs = CurrentLegislators()
    for legislator in currlegs:
        print legislator.most_recent_state, legislator.official_name
