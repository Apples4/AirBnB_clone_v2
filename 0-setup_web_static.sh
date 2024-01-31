#!/usr/bin/env bash
# automate various step with nginx for a static webpage

sudo apt-get -y update
sudo apt-get -y upgrade
sudo apt-get -y install nginx
sudo mkdir -p /data/web_static/release/test
sudo mkdir -p /data/web_static/shared/
echo "test test" | sudo tee data/web_static/test/index.html
sudo ln -s /data/web_static/releases/test/ /data/web_static/current
sudo chown -R ubuntu:ubuntu /data/
sudo sed -i "/listen 80 default_server/a location /hbnd_static { alias /data/web_static/current/;}" /etc/nginx/sites-enabled/default
sudo service nginx restart
