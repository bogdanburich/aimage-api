FROM python:3.8
WORKDIR /app
COPY . ./
RUN apt-get update && apt-get install -y python3-psycopg2
RUN python -m pip install --upgrade pip
RUN pip install -r requirements.txt --no-cache-dir
ENTRYPOINT ["gunicorn", "aimage.wsgi:application", "--bind", "0:8000"]
