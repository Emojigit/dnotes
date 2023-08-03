FROM python:3.11.4
ENV PYTHONUNBUFFERED 1
LABEL org.opencontainers.image.authors="root@1f616emo.xyz"
LABEL org.opencontainers.image.description="Note-taking website based on Django"

WORKDIR /usr/src/app

COPY requirements.txt /usr/src/app/
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

WORKDIR /usr/src/app/dnotes

EXPOSE 80/tcp
CMD [ "python", "manage.py", "runserver", "0.0.0.0:80" ]