FROM python:3.9-slim

RUN apt update
RUN apt install -y gcc default-libmysqlclient-dev

RUN pip install --upgrade pip
RUN pip install schedule mysqlclient pandas

CMD ["python3", "/app/main.py"]