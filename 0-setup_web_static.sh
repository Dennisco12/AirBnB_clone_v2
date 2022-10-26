#!/usr/bin/env bash
#This sets up my web server for the deployment of web_Static

sudo apt-get -y update
sudo apt-get -y upgrade

sudo apt-get -y install nginx
mkdir -p /data/web_static/
mkdir /data/web_static/releases/
mkdir /data/web_static/shared/
mkdir -p /data/web_static/releases/test/
touch /data/web_static/releases/test/index.html
echo "<html>
	<head>
	</head>
	<body>
        	<h1>Holberton School</h1>
	</body>
	</html>" > /data/web_static/releases/test/index.html
ln -sf /data/web_static/current /data/web_static/releases/test/
sudo chown -R ubuntu:ubuntu /data/
sed -i '48 i\ \tlocation /hbnb_static {\n\t\talias /data/web_static/current;\n\t}\n' /etc/nginx/sites-enabled/default
sudo service nginx restart
