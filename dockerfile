FROM python:3.12-alpine3.18

ENV PYTHONBUFFERED=1

COPY ./requirements.txt /django/requirements.txt

RUN pip install -r /django/requirements.txt

COPY ./QUurls /django

COPY ./QUurls/QUurls/manage.py /django

WORKDIR /django

CMD [ "python", "manage.py", "runserver", "0.0.0.0:8000" ]
