FROM python:3.11-alpine

WORKDIR /docker_system_dashboard
COPY . .
RUN apk add --no-cache python3 postgresql-libs && apk add --no-cache --virtual .build-deps gcc python3-dev musl-dev postgresql-dev
RUN pip3 install -r requirements.txt
CMD ["python3", "app.py"]