## Todos
correct spelling
add link to github

Add the following references
by individuals I intend to reference the basketball incident

Stay Rational
https://en.minghui.org/html/articles/2020/3/20/183715.html

Thirteen Methods of Torture Used in Today's China
http://www.clearharmony.net/articles/a25608-Thirteen-Methods-of-Torture-Used-in-Today-s-China.html#.Xq71t5pRW00

 The Dangers of the World's Dependence on China for Drugs and Medical Supplies 
http://en.minghui.org/html/articles/2020/4/2/183874.html

 CCP Publishes New Book to Praise Itself for Its Handling of the Coronavirus Epidemic 
http://en.minghui.org/html/articles/2020/3/5/183520.html

 Chinese Communist Party's Coronavirus Numbers Don't Add Up 
http://en.minghui.org/html/articles/2020/4/20/184118.html

 Canadian Lawmakers and Scholar Express “Serious Concerns” About WHO and Its Relationship with the Chinese Communist Party
 http://en.minghui.org/html/articles/2020/4/23/184155.html

 Three Plagues in the Ancient Roman Empire
 http://en.minghui.org/html/articles/2020/2/4/183093.html

 Why Did the Plagues of Ancient Rome Suddenly Disappear? 
http://en.minghui.org/html/articles/2020/2/10/183177.html

 Lessons from the CCP’s Orders to Destroy Virus Samples and Withhold Pandemic Information
 http://en.minghui.org/html/articles/2020/4/27/184217.html

 Expert Exposes China’s ‘Horrific’ Organ Harvesting: ‘The Victim is Still Alive and Breathing’ 
 http://en.minghui.org/html/articles/2019/5/29/177832.html

  Some Coronavirus Information That Can Help in Truth-Clarification
  http://en.minghui.org/html/articles/2020/2/12/183212.html

                <!-- <a target="_blank" href="https://www.androidauthority.com/huawei-vs-united-states-990007/">privacy</a> -->
Taken from how communism rules over the world

The communist movement not only deprives people of their lives, but also leads to enormous destruction of traditional values and culture. In particular, in communist China, moral standards have already dropped to a horrifying degree, far beyond what one can easily imagine. The harvesting of organs from living people, good people who practice self-cultivation, has become a state-sanctioned industrial operation. Communists have turned humans into monsters. Medical personnel, who are supposed to help the sick, have become demonic murderers. The CCP’s evil has reached across the world. Countries that are supposed to be upholding human rights are enticed with economic incentives to turn a blind eye.


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
