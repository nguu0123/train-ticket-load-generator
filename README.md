# train-ticket-auto-query

Train Ticket Auto Query Python Scripts

## How to use

- Install uv

```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
```

- Start load generator

```bash
uv sync
source .venv/bin/activate

locust --host http://localhost:8080 --headless --only-summary --users 2 -f main.py

locust --host http://localhost:8080 --headless --only-summary --users 2 -f main-admin.py
```
