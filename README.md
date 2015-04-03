# SourceSage-Backend-Python-

fixfit API


### Setup

For development, you should set up & run local MySQL, virtual environment

```
# install python dependencies
(.venv) $ pip install -r requirements.txt
```

Update the DB setting information on the the fixfit/settings.py file (refer fixfit/settings.py.sample or more information)

```
(.venv) $ PYTHONPATH=. python scripts/setup_db.py
```

### Run the server

```
chmod +x run
./run
```
