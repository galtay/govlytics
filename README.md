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

To test the installation, run the `legislators.py` file in the `src` directory. 
This should print the name and state of each senator. 

```bash
> python src/legislators.py
```

## Data 

Data on members of congress comes from https://github.com/unitedstates/congress-legislators


## Tools 

### http://neo4j.com/
  
A script is provided to install Neo4j.  It will appear to stall, but it is waiting
for you to type in your sudo password. After it finished you can point a web browser
at `http://localhost:7474`.  The default username and password are both `neo4j`.  On 
the first login it will ask you to change the password.  Change it to `neo`. 
