FROM python:3.7-stretch

COPY ./ /app
WORKDIR /app

RUN pip install -U pip gunicorn
RUN pip install -r requirements.txt

EXPOSE 8000
ENTRYPOINT ["gunicorn", "-b", ":8000", "runner.api:runner_api"]
