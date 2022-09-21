FROM tiangolo/uvicorn-gunicorn-fastapi:python3.9-slim

RUN apt update
RUN apt install -y gcc default-libmysqlclient-dev

RUN pip install --upgrade pip
RUN pip install mysqlclient

CMD ["uvicorn", "main:app", "--reload", "--host", "0.0.0.0"]