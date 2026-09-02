# Python OJ System

程序设计训练（Python）实验二：在线评测系统。

## Development Environment

- Ubuntu 22.04 on WSL 2
- Python 3.10+
- FastAPI
- Uvicorn
- Pytest
- Streamlit

## Setup

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements-dev.txt
Run Backend
uvicorn app.main:app --reload
API documentation:
http://127.0.0.1:8000/docs
Run Tests
pytest -q