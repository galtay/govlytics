# run with sudo privileges
add-apt-repository ppa:openjdk-r/ppa
apt-get update
apt-get install openjdk-8-jdk
update-alternatives --config java
update-alternatives --config javac
