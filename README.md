# pgtools
Postgresql sample code
Install Ubuntu 18.04

$ sudo apt update
$ sudo apt upgrade

Install sublime text 3

$ sudo snap install sublime-text --classic
$ sudo snap install pycharm-community --classic

Install python3 venv, create venv called pg1, activate it

$ sudo apt install python3-venv
$ python3 -m venv pg1
$ . pg1/bin/activate

pip install jupyter

$ sudo apt install postgresql postgresql-contrib python3-dev libpg-dev build-essential

  .
  .
  .
Success. You can now start the database server using:

  /usr/lib/postgresql/10/bin/pg_ctl -D /var/lib/postgresql/10/main -l logfile start

Ver Cluster Port Status Owner    Data directory              Log file
10  main    5432 down   postgres /var/lib/postgresql/10/main /var/log/postgresql/postgresql-10-main.log
update-alternatives: using /usr/share/postgresql/10/man/man1/postmaster.1.gz to provide /usr/share/man/man1/postmaster.1.gz (postmaster.1.gz) in auto mode
Setting up postgresql (10+190) ...
Setting up postgresql-contrib (10+190) ...
Processing triggers for ureadahead (0.100.0-21) ...
Processing triggers for systemd (237-3ubuntu10.21) ...

user1@postgres1:~$ sudo -i -u postgres
postgres@postgres1:~$ psql
psql (10.7 (Ubuntu 10.7-0ubuntu0.18.04.1))
Type "help" for help.

postgres=# \q


. pg1/bin/activate
pip install sqlalchemy

sudo apt install python-psycopg2
pip install psycopg2



createuser --interactive --pwprompt

createdb -O user1 mydb

python
>>> import sqlalchemy as db
>>> engine = db.create_engine('postgresql://user1:user1@localhost/mydb')
>>> 
