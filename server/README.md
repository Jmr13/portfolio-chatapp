# Installation

## Create a virtual environment
```
py -m venv venv  
venv\Scripts\activate # On Linux: source venv/bin/activate
```

## Install dependencies
```
pip install -r requirements.txt
```

# Running the App
## Start the FastAPI server
```
uvicorn app.main:app --reload
```

Visit http://localhost:8000/docs for Swagger UI

Visit http://localhost:8000/redoc for ReDoc