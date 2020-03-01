FROM ubuntu

RUN apt update
RUN apt install -y python python-pip 

RUN apt update
RUN apt install tesseract-ocr -y
RUN apt install libtesseract-dev -y



COPY . /opt/digidoc/


RUN pip install -r /opt/digidoc/requirements.txt


ENTRYPOINT python /opt/digidoc/app.py 