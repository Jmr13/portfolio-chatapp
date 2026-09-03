# Installation

## Create a virtual environment
From the `server/` directory:

```bash
python3 -m venv .venv
source .venv/bin/activate   # Windows: .venv\Scripts\activate
```

## Install dependencies
```bash
pip install -r requirements.txt
```

## Configure environment variables
Create a local `.env` file in `server/` based on `.env.example` and provide the Azure OpenAI, resume, and admin configuration values used by the backend.

# Running the App
## Start the FastAPI server
```bash
uvicorn app.main:app --reload
```

Visit http://localhost:8000/docs for Swagger UI.

Visit http://localhost:8000/redoc for ReDoc.