## Todos
by individuals I intend to reference the basketball incident

 The Dangers of the World's Dependence on China for Drugs and Medical Supplies 
http://en.minghui.org/html/articles/2020/4/2/183874.html

 CCP Publishes New Book to Praise Itself for Its Handling of the Coronavirus Epidemic 
http://en.minghui.org/html/articles/2020/3/5/183520.html

“

Why this no work
            <table style="text-align:right">
                <tr>
                    <td>Email</td>
                    <td><a href="mailto:peteris.ratnieks@gmail.com">peteris.ratnieks@gmail.com</a></td>
                </tr>
                <tr>
                    <td>Keybase</td>
                    <td><a href="https://keybase.io/peteris_ratnieks">peteris_ratnieks</a></td>
                </tr>
            </table>

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
