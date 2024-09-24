FROM python:3-alpine3.12
WORKDIR /app
COPY . /app
RUN pip3 install --upgrade pip && pip3 install -r requirements.txt
EXPOSE 8080
CMD python ./app.py