"""Module to handle data fetching.
"""

import os
import logging
import subprocess

GOVLYTICS_CONF_DIR = os.path.join(os.getenv('HOME'), '.govlytics')
GOVLYTICS_DATA_DIR = os.getenv(
    'GOVLYTICS_DATA_DIR',
    os.path.join(GOVLYTICS_CONF_DIR, 'data')
)

GITHUB_BASE = 'https://github.com/unitedstates'

CONGRESS_REPO = os.path.join(
    GITHUB_BASE, 'congress.git')

CONGRESS_LEGISLATORS_REPO = os.path.join(
    GITHUB_BASE, 'congress-legislators.git')

CONGRESS_LEGISLATORS_CURRENT_FNAME = os.path.join(
    GOVLYTICS_DATA_DIR,
    'congress-legislators',
    'legislators-current.yaml')


def fetch():
    """Launch data getting UI."""
    _ui_loop()


def _get_congress_legislators():
    """Refresh congress legislators data."""
    data_path = os.path.join(
        GOVLYTICS_DATA_DIR, 'congress-legislators')

    logging.info('refreshing congress-legislators ...')
    if os.path.isdir(data_path):
        logging.info(
            'data_path: {} exists.  performing git pull'.format(data_path))
        subprocess.call(['git', '-C', data_path, 'pull'])
    else:
        logging.info(
            'data_path: {} does not exist.  cloning repo {}'.format(
                data_path, CONGRESS_LEGISLATORS_REPO))
        subprocess.call([
            'git', 'clone', CONGRESS_LEGISLATORS_REPO, data_path])


def _get_congress():
    """Refresh congress repo."""
    data_path = os.path.join(
        GOVLYTICS_DATA_DIR, 'congress')

    logging.info('refreshing congress ...')
    if os.path.isdir(data_path):
        logging.info(
            'data_path: {} exists.  performing git pull'.format(data_path))
        subprocess.call(['git', '-C', data_path, 'pull'])
    else:
        logging.info(
            'data_path: {} does not exist.  cloning repo {}'.format(
                data_path, CONGRESS_REPO))
        subprocess.call([
            'git', 'clone', CONGRESS_REPO, data_path])


def _get_bills():
    """Refresh congress repo."""
    congress_path = os.path.join(GOVLYTICS_DATA_DIR, 'congress')
    logging.info('getting bills ...')
    subprocess.call([os.path.join(congress_path, 'run'), 'bills'])


def _print_menu():
    print
    print 28 * "=" , "Govlytics Data Menu" , 28 * "="
    print
    print '* govlytics conf dir: {}'.format(GOVLYTICS_CONF_DIR)
    print '* govlytics data dir: {}'.format(GOVLYTICS_DATA_DIR)
    print
    print "1) clone/update congress-legislators"
    print "2) clone/update congress"
    print "3) get bills (current congress, long download)"
    print "x) exit"
    print 67 * "-"

def _ui_loop():

    loop=True

    while loop:
        _print_menu()
        choice = raw_input("Enter your choice [1, 2, 3, x]: ")

        if choice=='1':
            _get_congress_legislators()
        elif choice=='2':
            _get_congress()
        elif choice=='3':
            _get_bills()
        elif choice=='x':
            print "Menu x has been selected"
            loop=False
        else:
            raw_input(
                "Wrong option selection. Enter any key to try again ...")


if __name__ == '__main__':
    _ui_loop()
