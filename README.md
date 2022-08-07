```console

docker run -d -p 5432:5432 --name demodb -e POSTGRES_PASSWORD=Passw0rd123 postgres:latest

python3 -m venv todo
. todo/bin/activate

pip install Flask
pip install Flask-SQLAlchemy 
pip install python-dotenv
pip install psycopg2-binary

export FLASK_APP=app.py
export FLASK_ENV=development
flask run
```
