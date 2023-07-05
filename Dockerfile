FROM tiangolo/uvicorn-gunicorn-fastapi:python3.10

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY . /app

#CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "80", "--reload"]
