# Tone & Intent Analyzer API (with Gemini + Django)

This Django REST API takes in user queries, analyzes the **tone** and **intent** using Google's Gemini AI model, and suggests relevant actions like ordering food, finding recipes, asking for help, or sharing news.

## Tech Stack
- **Python 3.10**
- **Django 5.2**
- **DjangoRestFramework**
- **Google Generative AI (Gemini)**
- **PostgreSQL**
- **dotenv**

## Setup & Installation

### Step 1 - Git Clone
```
git clone https://github.com/17prateek12/tone_analyzer
````

### Step 2
```
cd tone_analyzer
```

### Step 3 - Create virtual environment and Activate it
```
Python -m virtualenv <env_name>
<env_name>/scripts/activate .
```

### Step 4 - Install required libraries
```
pip install -r requirements.txt
```
or
```
pip install -U -q google-genai
pip install django djangorestframework psycopg2 python-dotenv
```

### Step 5 - Set up .env file
```
GOOGLE_API_KEY = 
DJANGO_SECRET_KEY = 
POSTGRES_NAME = 
POSTGRES_ENGINE = 
POSTGRES_USER = 
POSTGRES_PASSWORD = 
POSTGRES_HOST = 
POSTGRES_PORT = 
```

### Step 6 - Make migrations
```
python manage.py makemigrations
python manage.py migrate
```

### Step 7 - RunServer
```
python manage.py runserver
```

The server will run
```
http://127.0.0.1:8000
```

### API URL
```
http://127.0.0.1:8000/api/analyze/
```
METHOD = POST 
Test inside postman

## Sample Response

### Sample Request 1
```
{
    "query":"how make pizza"
}
```

### Sample Response 1
```
{
    "query": "how make pizza",
    "analysis": {
        "tone": "Informative",
        "intent": "Request for instructions"
    },
    "suggested_actions": [
        {
            "action": "FIND_RECIPE",
            "display_text": "Find Food Recipes"
        }
    ]
}
```

### Sample Request 2
```
{
    "query":"what can i do in career?"
}
```

### Sample Response 2
```
{
    "query": "what can i do in career?",
    "analysis": {
        "tone": "Neutral",
        "intent": "Career guidance/exploration"
    },
    "suggested_actions": [
        {
            "action": "ASK_HELP",
            "display_text": "Ask for Help"
        }
    ]
}
```
