# Inventory Management System

A full-stack inventory management web app built with **FastAPI**, **PostgreSQL**, and **MongoDB**. It lets you add, view, edit, and delete inventory items through a clean dark-themed UI, while automatically logging every API action to MongoDB for auditing.

---

## Features

- **CRUD inventory management** — add, view, edit, and delete items with name, description, price, and stock quantity
- **Live API activity log** — every request is recorded in MongoDB and shown in the UI with timestamp, method, action, and user agent
- **Dark-themed frontend** — single-page UI served directly by FastAPI (no separate frontend server needed)
- **Auto-documented REST API** — interactive Swagger docs available at `/docs`

---

## Tech Stack

| Layer | Technology |
|---|---|
| Backend | [FastAPI](https://fastapi.tiangolo.com/) + [Uvicorn](https://www.uvicorn.org/) |
| Inventory DB | PostgreSQL 16 (via SQLAlchemy) |
| Logging DB | MongoDB 7.0 (via Motor — async driver) |
| Frontend | Vanilla HTML/CSS/JS (served by FastAPI) |
| Containerization | Docker + Docker Compose |

---

## Project Structure

```
.
├── main.py           # FastAPI app, routes, and request logging middleware
├── table.py          # SQLAlchemy ORM model (Item table)
├── database.py       # PostgreSQL connection and session setup
├── mongo.py          # MongoDB connection setup
├── bouncer.py        # Pydantic schemas for request/response validation
├── index.html        # Frontend UI
├── Dockerfile        # Container definition for the FastAPI app
├── docker-compose.yml # Orchestrates FastAPI + PostgreSQL + MongoDB
└── requirements.txt  # Python dependencies
```

---

## Prerequisites

- [Docker](https://docs.docker.com/get-docker/) and [Docker Compose](https://docs.docker.com/compose/install/) installed on your machine

---

## Running Locally with Docker

**1. Clone the repository**

```bash
git clone https://github.com/your-username/your-repo-name.git
cd your-repo-name
```

**2. Start all services**

```bash
docker compose up --build
```

This spins up three containers:
- `inventory_api` — the FastAPI app on port **8000**
- `inventory_postgres` — PostgreSQL on port **5422**
- `inventory_mongo` — MongoDB on port **27017**

**3. Open the app**

Visit [http://localhost:8000](http://localhost:8000) in your browser.

Interactive API docs are available at [http://localhost:8000/docs](http://localhost:8000/docs).

**4. Stop the app**

```bash
docker compose down
```

To also delete the stored data volumes:

```bash
docker compose down -v
```

---

## API Endpoints

| Method | Endpoint | Description |
|---|---|---|
| `GET` | `/` | Serves the frontend UI |
| `GET` | `/items` | List all inventory items |
| `POST` | `/item` | Create a new item |
| `GET` | `/item/{id}` | Get a single item by ID |
| `PUT` | `/item/{id}` | Update an item by ID |
| `DELETE` | `/item/{id}` | Delete an item by ID |
| `GET` | `/logs` | Retrieve recent API activity logs |

## Configuration

Database credentials are managed via a `.env` file, which is **not** committed to this repo.
To run the project, create a `.env` file in the project root with the following variables:

```bash
POSTGRES_USER=your_username
POSTGRES_PASSWORD=your_password
POSTGRES_DB=inventory_db
MONGO_ROOT_USERNAME=your_username
MONGO_ROOT_PASSWORD=your_password
```


 
