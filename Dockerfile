FROM ubuntu:18.04
LABEL org.opencontainers.image.authors="rudtjs4540@gmail.com"

RUN apt-get update -y
RUN apt-get install -y python3-pip python3-dev ffmpeg libsm6 libxext6 libxrender-dev

COPY ./requirements.txt /app/requirements.txt
WORKDIR /app

RUN pip3 install --upgrade pip
RUN pip3 install -r requirements.txt
COPY . /app

ENTRYPOINT [ "python3" ]
CMD [ "object_tracker.py" ]
