"""Deletes the current graph."""
from py2neo import Graph, Node, Relationship

username='neo4j'
password='neo'
graph = Graph("http://{}:{}@localhost:7474/db/data".format(
    username, password))
graph.delete_all()
