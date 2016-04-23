"""Test install and data fetch."""

import govlytics

currlegs = govlytics.gov.legislators.CurrentLegislators()
for leg in currlegs:
    if leg.most_recent_state == 'IL':
        print(leg.most_recent_state, leg.official_name)
