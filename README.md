# Digitalize Paper Documents

### General use cases

-   Making paper documents searchable
-   Modifying in digital form
-   Making copy from image
-   Get summary of large photo document
-   Different type of entity extration
-   Keyword extraction

### Installation

* Install [Docker](https://docs.docker.com/install/)
* Pull `shivampip/digidoc` docker image
```
docker pull shivampip/digidoc
```
* Run the container 
```
docker run -d -p 5000:5000 shivampip/digidoc
```

* Open [localhost:5000](http://localhost:5000) in browser. (in case of remote server, use server ip)

### Screenshots

![Home](/imgs/raw/11.png)
![Text Extraction](/imgs/raw/22.png)
![Doc identified](/imgs/raw/33.png)

