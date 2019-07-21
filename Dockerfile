FROM python:3.7

USER root

WORKDIR /app

ADD . /app

RUN pip install --trusted-host pypi.python.org -r requirements.txt

EXPOSE 8000

CMD ["gunicorn", "-c", "gunicorn.py", "app:server"]