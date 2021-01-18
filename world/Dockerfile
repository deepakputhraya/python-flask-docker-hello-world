FROM python:3.6

LABEL version="4.0"
LABEL author="deepakputhraya"
LABEL appname="python-world"

COPY . /app
WORKDIR /app
RUN pip install -r requirements.txt
ENTRYPOINT ["python"]
CMD ["app.py"]
EXPOSE 4000
