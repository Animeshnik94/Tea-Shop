python3 manage.py dumpdata goods.Products > fixtures/goods/prod.json
python3 manage.py loaddata fixtures/goods/prod.json

sudo -u postgres psql - Эта команда запускает psql от имени пользователя postgres, 
который является суперпользователем по умолчанию в PostgreSQL.

psql -U имя_пользователя -d имя_базы_данных - Если вы создали других пользователей в PostgreSQL 
и хотите подключиться от их имени, используйте следующую команду

------------------------
sudo -u postgres psql

CREATE USER newuser WITH PASSWORD 'password';
ALTER USER newuser CREATEDB;
CREATE DATABASE mydatabase;
GRANT ALL PRIVILEGES ON DATABASE mydatabase TO newuser;

\q
-------------------------