
# Dockerfile 04/2021
# Python environment for exporting data analysis for processing on remote systems.

FROM python:3.8.5
MAINTAINER Alex Perkins <a.j.p.perkins@sms.ed.ac.uk>

RUN mkdir /api_test
WORKDIR /api_test
ADD requirements.txt /api_test/
RUN pip install -r requirements.txt
ADD . /api_test/

EXPOSE 4000

ENTRYPOINT ["/bin/bash"]
