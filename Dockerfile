FROM python:3.6.3-slim

COPY ./ /app
WORKDIR /app

RUN pip install -U pip gunicorn
RUN pip install -r requirements.txt

EXPOSE 8000
ENTRYPOINT ["gunicorn", "-b", ":8000", "runner.api:api"]
