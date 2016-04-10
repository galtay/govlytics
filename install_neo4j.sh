wget -O - https://debian.neo4j.org/neotechnology.gpg.key | apt-key add -
echo 'deb http://debian.neo4j.org/repo stable/' > /tmp/neo4j.list
mv /tmp/neo4j.list /etc/apt/sources.list.d
apt-get update
apt-get install neo4j
