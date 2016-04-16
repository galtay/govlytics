# govlytics
Playing with government data

## Installation

This package was tested on Ubuntu 15.10 64 bit with python 2.7.10.
For best results create a virtual environment,

```bash
> virtualenv venv
> source venv/bin/acticate
> pip install -r requirements.txt
```

To test the installation, run the `0_test_install.py` file in the `src`
directory.  This should print the name of each representative from IL.

```bash
> python src/0_test_install.py
```

## Data

The `src/0_test_install.py` script used data that was bundled with this
package in the `test_data` directory.  However, the fine folks at
www.govtrack.us have made a very large amount of data available to the
public.  To work with their data I find it convenient to clone their
repos in a `data` directory inside this package.  The `.gitignore` file
in this package already includes an entry that will ignore this `data`
directory.

   - Data on members of congress comes from https://github.com/unitedstates/congress-legislators

   - Data on actions of congress comes from https://github.com/unitedstates/congress

These repos can be cloned into the `data` directory using the following
commands,

```bash
> mkdir data
> cd data
> git clone https://github.com/unitedstates/congress.git
> git clone https://github.com/unitedstates/congress-legislators.git
```

The data about congress legislators is small enough that the `.yaml` files
that store it are included in the `congress-legislators` repo.
The data available through the `congress` repo is larger and must be
fetched by running commands.  To fetch data, first install the requirements
of the `congress` repo.

```bash
> cd data/congress
> pip install -r requirements.txt
```

You should now be able to fetch datasets using the `run` command
(see https://github.com/unitedstates/congress#collecting-the-data).
For example we can fetch the bills data for the most recent
congress using the following commands,

```bash
> ./run bills
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
change the password.  Change it to `neo`.
