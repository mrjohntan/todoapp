FROM python:3.10.6-slim-bullseye

COPY ./requirements.txt /app/requirements.txt

WORKDIR /app

RUN pip install -r requirements.txt

COPY templates /app/templates

COPY .env app.py config.py /app/

ENTRYPOINT [ "python" ]

CMD [ "app.py" ]