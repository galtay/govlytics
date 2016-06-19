"""Module to handle data fetching.
"""

from __future__ import print_function
import os
import logging
import subprocess

# main govlytics directories
#=====================================================================
GOVLYTICS_CONF_DIR = os.path.join(os.getenv('HOME'), '.govlytics')
GOVLYTICS_DATA_DIR = os.getenv(
    'GOVLYTICS_DATA_DIR',
    os.path.join(GOVLYTICS_CONF_DIR, 'data')
)


# github repos for data
#=====================================================================
GITHUB_BASE = 'https://github.com/unitedstates'

CONGRESS_REPO = os.path.join(
    GITHUB_BASE, 'congress.git')

CONGRESS_LEGISLATORS_REPO = os.path.join(
    GITHUB_BASE, 'congress-legislators.git')


# directories and file names in repos cloned to govlytics data directory
#=====================================================================
CONGRESS_LEGISLATORS_PATH = os.path.join(
    GOVLYTICS_DATA_DIR, 'congress-legislators')

CONGRESS_LEGISLATORS_CURRENT_FNAME = os.path.join(
    CONGRESS_LEGISLATORS_PATH, 'legislators-current.yaml')

CONGRESS_PATH = os.path.join(GOVLYTICS_DATA_DIR, 'congress')
CONGRESS_DATA_PATH = os.path.join(CONGRESS_PATH, 'data')



def fetch():
    """Launch data getting UI."""
    _ui_loop()


def create_govlytics_dirs():
    """Checks if the base govlytics directories exist and creates them
    if they dont."""
    if not os.path.isdir(GOVLYTICS_CONF_DIR):
        logging.info(
            'govlytics conf directory {} doesnt exist, creating ... '.
            format(GOVLYTICS_CONF_DIR))
        subprocess.call(['mkdir', '-p', GOVLYTICS_CONF_DIR])
    if not os.path.isdir(GOVLYTICS_DATA_DIR):
        logging.info(
            'govlytics data directory {} doesnt exist, creating ... '.
            format(GOVLYTICS_DATA_DIR))
        subprocess.call(['mkdir', '-p', GOVLYTICS_DATA_DIR])


def _get_congress_legislators():
    """Refresh congress legislators data."""
    data_path = CONGRESS_LEGISLATORS_PATH
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
    data_path = CONGRESS_PATH

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
    """Refresh congress repo.  We want this command executed from
    the congress repo directory."""
    if not os.path.isdir(CONGRESS_PATH):
        _get_congress()
    logging.info('getting bills ...')
    subprocess.call(
        [os.path.join(CONGRESS_PATH, 'run'), 'bills'],
        cwd=CONGRESS_PATH)


def _print_menu():
    print()
    print(28 * '=' , 'Govlytics Data Menu' , 28 * '=')
    print()
    print('* govlytics conf dir: {}'.format(GOVLYTICS_CONF_DIR))
    print('* govlytics data dir: {}'.format(GOVLYTICS_DATA_DIR))
    print()
    print('1) clone/update congress-legislators')
    print('2) get bills (current congress, long download)')
    print('x) exit')
    print( 67 * '-')

def _ui_loop():

    loop=True

    while loop:
        _print_menu()
        choice = input('Enter your choice [1, 2, x]: ')

        if choice=='1':
            _get_congress_legislators()
        elif choice=='2':
            _get_bills()
        elif choice=='x':
            print('Menu x has been selected')
            loop=False
        else:
            input(
                'Wrong option selection. Enter any key to try again ...')


if __name__ == '__main__':
    _ui_loop()
