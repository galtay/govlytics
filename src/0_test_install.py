"""Test install with bundled data."""

import os
import legislators

if __name__ == '__main__':
    path_here = os.path.dirname(os.path.abspath(__file__))
    test_data_path = os.path.join(path_here, '..', 'test_data')
    legcurr_fname = os.path.join(test_data_path, 'legislators-current.yaml')

    print 'attempting to read {} ... '.format(legcurr_fname)
    currlegs = legislators.CurrentLegislators(legcurr_fname)
    print 'success'
    print
    reps = currlegs.return_by_type('rep')
    print 'current representatives from IL are ...'
    for rep in reps:
        if rep.return_most_recent_state() == 'IL':
            print rep.return_official_name()
