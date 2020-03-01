FROM ubuntu

RUN apt update
RUN apt install -y python3 python3-pip 

RUN apt update
RUN apt install tesseract-ocr -y
RUN apt install libtesseract-dev -y
RUN apt-get install -y libsm6 libxext6 libxrender-dev

RUN pip3 install -U pip 

COPY . /opt/digidoc/


RUN pip3 install -r /opt/digidoc/requirements.txt


ENTRYPOINT python3 /opt/digidoc/app.py 