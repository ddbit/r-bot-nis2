# Rag PoC with LLamaIndex

## Instructions

Create a python environment and activate it

```
python -m venv .flaskenv
source .flaskenv/bin/activate
```

Upgrade pip 
```
pip install --upgrade pip
```

Then install Flask and the other dependencies

```
pip install flask flask_cors openai
```

Then run the app
```
flask --app teller.app  run
```

You can now connect to 
```
http://127.0.0.1:5000/
```
