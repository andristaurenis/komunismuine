

## Deployment

Run this as root on your ubuntu machine:
```
apt-get update && apt-get upgrade
apt-get install python3-wheel python3-dev build-essential gcc nginx

cd /var/www
git clone https://github.com/andristaurenis/komunismuine

mkdir -p /var/log/uwsgi
chown -R www-data:www-data /var/log/uwsgi/
chown -R www-data:www-data /var/www/komunismuine/

cd komunismuine/
python3 -m venv venv
. venv/bin/activate
pip install -r stable-req.txt

rm /etc/nginx/sites-enabled/default
ln /var/www/komunismuine/komunismuine_nginx.conf /etc/nginx/sites-available/
ln /etc/nginx/sites-available/komunismuine_nginx.conf /etc/nginx/sites-enabled/

/etc/init.d/nginx restart

mkdir -p /etc/uwsgi/vassals
ln /var/www/komunismuine/komunismuine_uwsgi.ini /etc/uwsgi/vassals

echo "
#!/bin/bash
set -e

cd /var/www/komunismuine
. venv/bin/activate
uwsgi --ini /var/www/komunismuine/komunismuine_uwsgi.ini &
" > /root/startflask.sh
chmod +x /root/startflask.sh

/root/startflask.sh
```
