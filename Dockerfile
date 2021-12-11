FROM python:3
# Import Python runtime and set up working directory

MAINTAINER Akanksha Vishwakarma

RUN apt-get update
##In alpine we use apk to install things whereas in ubuntu we use apt-get to install things
RUN pip install --upgrade pip
# Import Python runtime and set up working directory
WORKDIR /app

COPY . /app

RUN python3 -m pip install --user --no-cache-dir -r requirements.txt
#write command $ pip freeze > requirement.txt to automatically create requirement.txt file containing all the required packages & dependencies.

EXPOSE  5000
#here port 5000 is exposed so that the docker file can be accesed from outside world.
# Open port 5000 for serving the webpage

#ENTRYPOINT ["python3"]

CMD ["python", "main.py"]
