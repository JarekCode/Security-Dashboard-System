FROM python:3.11-alpine

WORKDIR /docker_system_dashboard
COPY . .
RUN pip3 install -r requirements.txt
CMD ["python3", "app.py"]