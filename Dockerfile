FROM ubuntu:20.04

RUN sed -i 's@archive.ubuntu.com@ftp.jaist.ac.jp/pub/Linux@g' /etc/apt/sources.list
RUN apt-get update
RUN apt-get install -y python3 python3-pip

CMD ["/bin/bash", "which", "python3"]

