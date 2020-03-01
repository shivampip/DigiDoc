FROM ubuntu

RUN apt update
RUN apt install -y python python-pip 

RUN apt update
RUN apt install tesseract-ocr -y
RUN apt install libtesseract-dev -y

RUN pip install -r /opt/digidoc/requirements.txt


COPY . /opt/digidoc/

ENTRYPOINT python /opt/digidoc/app.py 