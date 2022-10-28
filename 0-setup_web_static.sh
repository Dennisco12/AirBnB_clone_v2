#!/usr/bin/env bash
#This sets up my web server for the deployment of web_Static

sudo apt-get -y update > /dev/null

#install nginx
sudo apt-get -y install nginx
sudo service nginx start

#configure the file directories
sudo mkdir -p /data/web_static/
sudo mkdir /data/web_static/releases/
sudo mkdir /data/web_static/shared/
sudo mkdir -p /data/web_static/releases/test/
touch /data/web_static/releases/test/index.html
echo "<html>
	<head>
	</head>
	<body>
        	<h1>Holberton School</h1>
	</body>
	</html>" | sudo tee /data/web_static/releases/test/index.html > /dev/null
sudo ln -sf /data/web_static/releases/test/ /data/web_static/current

#set owners
sudo chown -R ubuntu:ubuntu /data/

#configure nginx
sudo sed -i '44i \\n\tlocation /hbnb_static {\n\t\talias /data/web_static/current;\n\t}' /etc/nginx/sites-available/default

#restart nginx
sudo service nginx restart
