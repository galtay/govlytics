"""Test install with bundled data."""

import os
import legislators


def main():
    path_here = os.path.dirname(os.path.abspath(__file__))
    test_data_path = os.path.join(path_here, '..', 'test_data')
    legcurr_fname = os.path.join(
        test_data_path, 'congress-legislators', 'legislators-current.yaml')

    print 'attempting to read {} ... '.format(legcurr_fname)
    currlegs = legislators.CurrentLegislators(legcurr_fname)
    print 'success'
    print
    print 'current representatives from IL are ...'
    for rep in currlegs.representatives:
        if rep.most_recent_state == 'IL':
            print rep.official_name


if __name__ == '__main__':
    main()
