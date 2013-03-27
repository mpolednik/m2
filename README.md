#M2

Maturitní projekt fotogalerie

##Provoz pomocí virtuálního systému

* uživatel: root, m2
* heslo: maturita (stejné pro oba)
* Import pomoci VirtualBox -> Import Appliance
* Start přes VirtualBox GUI nebo VBoxHeadless --startvm {m2}

###Automatický provoz

Systém je připraven k použití po spuštění - všechny service automaticky naběhnout (příp. zjistit IP u bridged mode)

/etc/nginx/nginx.conf

    listen: 80;

###Manuální provoz

Je potřeba spustit service mysqld, memcached, nginx a supervisord

    service mysqld start
    service memcached start
    service nginx start
    service supervisord start
V případě nefunkčnosti service supervisord lze aplikaci spustit i manuálně

    /usr/local/bin/python2.7 /var/www/m2/application.py

##Manuální instalace

###Potřebný software

* Operační systém na bázi UNIXu (teoreticky Windows)
* Python 2.7.3
* nginx 1.2.26
* MySQL 5.5.29
* memcached 1.4.15

####Potřebné python moduly

* Flask==0.9
* Flask-Bcrypt==0.5.2
* Flask-KVSession==0.3.2
* Flask-LazyViews==0.4
* Flask-SQLAlchemy==0.16
* Flask-WTF==0.8.2
* Jinja2==2.6
* MySQL-python==1.2.4
* PIL==1.1.7
* SQLAlchemy==0.8.0b2
* WTForms==1.0.3
* Werkzeug==0.8.3
* itsdangerous==0.17
* psutil==0.6.1
* py-bcrypt==0.2
* python-memcached==1.48
* simplekv==0.5
* tornado==2.4.1
* urllib3==1.5
* wsgiref==0.1.2

###Konfigurace

####Nginx

/etc/nginx/nginx.conf (default, /usr/local/nginx/nginx.conf v předpřipraveném OS)

    client_max_body_size 50M;

    server {
        server_name  localhost;
        listen       80;

        location /static {
            alias /Users/mpolednik/Documents/m2/static;
        }

        location / {
            proxy_pass   http://127.0.0.1:8000;
        }
    }

####Mysqld

Žádné specifikcé požadavky na my.ini (ideálně použit production a maximalizovat cache)
Tvorba databáze, uživatele a nahrání dat (může být provozováno i pod root)

    mysql -u root -p
    > CREATE USER 'm2'@'%' IDENTIFIED BY 'maturita';
    > CREATE DATABASE m2;
    > GRANT ALL PRIVILEGES ON m2 . * TO 'maturita'@'%';
    mysql -u m2 -p m2 < sql/schema.sql
    mysql -u m2 -p m2 < sql/data.sql

####Aplikace

Databáze využívaná aplikací (defaultně data shodná s konfigurací mysqld)

    dbconf = {
        'user': 'm2',
        'pass': 'maturita',
        'name': 'm2',
        'host': 'localhost',
    }

Databáze serveru, na kterém běží sms handler

* local / global
* host: 192.168.171.11 / 95.82.149.75
* port 3306 / 9999

<!-- md fix -->

    smsconf = {
        'user': 'polema',
        'pass': 'maturita',
        'name': 'sms',
        'host': '95.82.149.75',
        'port': 9999,
    }

###Spouštění software stacku (příklad na obecném GNU/Linux OS)

    mysqld_safe &
    nginx
    memcached -D
    python /cesta/k/application.py

##Poznámky na konec

Sms login u administrace lze obejít přes backdoor zadáním kódu REALLY\_AWESOME\_BACKDOOR

Adresářová struktura (nutná pro korektní funkčnost)

    application.py
    app
        models
        views
        controllers
        helpers
    config
    static
        css
        js
        img
            thumb
            upload
    translation

Skript generator.py lze využít pro generování dalších náhodných dat, pro dané použití musí být upraven
