# govlytics

Playing with graph databases and government data.  Below is an example graph showing bills that were sponsored by democrats and co-sponsored by republicans.  Below that is the inverse (bills sponsored by republicans and co-sponsored by democrats)

 ![Ds](imgs/dem_spons_rep_cospons.jpg)

 ![Rs](imgs/rep_spons_dem_cospons.jpg)

## Installation

This package was tested on Ubuntu 15.10 64 bit with python 2.7.10.
For best results create a virtual environment.

### System Libraries

On Debian based systems you can install the system dependencies like so,

```bash
> sudo apt-get install python-dev python-virtualenv libyaml-dev libxml2-dev libxslt1-dev libz-dev
```

### Package Install

Now we can clone the repo, create a virtual environment, and build the package,

```bash
> git clone https://github.com/galtay/govlytics.git
> cd govlytics
> virtualenv venv
> source venv/bin/acticate
> pip install -r requirements.txt
> export PYTHONPATH='./'
```

To test the installation, run the `0_test_install.py` file in the `examples`
directory.  This should fetch a small amount of data and then print out the
current legislators from Illinois.

```bash
> python examples/0_test_install.py
```

## Data

The fine folks at www.govtrack.us have made a very large amount of data
available to the public.  Govlytics has some built in tools to fetch and
work with their data.  In fact, the `0_test_install.py` script makes use
of the `govlytics/gov/data_utils.py` module to clone a repo
(https://github.com/unitedstates/congress-legislators) that handles
data on congressional legislators and committees.

Govlytics will create a configuration directory in your home directory
called `.govlytics`.  By default, govlytics will store data that it fetches
in `.govlytics/data`.  You can change this default behaviour by setting
the environment variable `GOVLYTICS_DATA_DIR`.  In addition, you can
run a command line UI that will allow you to download data by running the
`govlytics/gov/data_utils.py` module,

```bash
> python govlytics/gov/data_utils.py
```


## Tools

### Neo4j (http://neo4j.com)

A script is provided to install Neo4j.  It has to be run with sudo privelages like so

```bash
> sudo bash ./install_neo4j.sh
```

It will prompt you for your sudo password and then install `neo4j` using the
commands given at the following link (http://debian.neo4j.org/). After it
finishes you can point a web browser at `http://localhost:7474`.  The default
username and password are both `neo4j`.  On the first login it will ask you to
change the password.  Change it to `neo4jgov`.
