# HelloWorld

A minimal Python 3.12 FastAPI app with Docker and Docker Compose support.

## Files

- `app.py` - FastAPI application with two routes.
- `requirements.txt` - only FastAPI and Uvicorn.
- `Dockerfile` - builds the app into a container.
- `compose.yaml` - starts the service locally on port `8000`.

## Local Python run

Install dependencies and run locally:

```bash
python3.12 -m pip install -r requirements.txt
uvicorn app:app --host 0.0.0.0 --port 8000
```

Then visit:

- `http://localhost:8000/` → `{ "message": "hello world" }`
- `http://localhost:8000/health` → `{ "status": "ok" }`

## Build and run with Docker

Build the image:

```bash
docker build -t helloworld-fastapi .
```

Run the container:

```bash
docker run --rm -p 8000:8000 helloworld-fastapi
```

## Run with Docker Compose

Start the service:

```bash
docker compose -f compose.yaml up --build
```

Stop it with:

```bash
docker compose -f compose.yaml down
```
