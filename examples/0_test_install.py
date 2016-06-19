"""Test install and data fetch."""

from __future__ import print_function
import govlytics

currlegs = govlytics.gov.legislators.CurrentLegislators()
for leg in currlegs:
    if leg.most_recent_state == 'IL':
        print(leg.most_recent_state, leg.official_name)
