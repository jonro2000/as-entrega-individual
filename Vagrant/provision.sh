apt-get -y update
apt-get -y upgrade
apt-get -y install nginx
apt -y install python3-pip
systemctl restart nginx
cd /home/vagrant/shared_folder
mkdir data
python3 ./app.py http://localhost/

