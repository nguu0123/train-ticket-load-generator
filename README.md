# train-ticket-auto-query

Train Ticket Auto Query Python Scripts

## How to use

```bash
python -m venv env
. env/bin/activate

pip install -r requirements.txt

locust --host http://localhost:8080 --headless --users 2 -f main.py
```
