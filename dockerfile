FROM python:3.12-alpine3.18

COPY ./requirements.txt /app/requirements.txt

RUN pip install -r /app/requirements.txt

COPY ./QUurls /app

WORKDIR /app

CMD [ "python", "manage.py", "runserver", "0.0.0.0:8000" ]
