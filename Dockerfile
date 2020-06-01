FROM ubuntu:20.04

RUN sed -i 's@archive.ubuntu.com@ftp.jaist.ac.jp/pub/Linux@g' /etc/apt/sources.list
RUN apt-get update
RUN apt-get install -y python3 python3-pip

RUN pip3 install jupyterlab
RUN pip3 install beautifulsoup4
RUN pip3 install gensim

WORKDIR /var/volume

CMD jupyter lab --ip=0.0.0.0 --no-browser --allow-root

