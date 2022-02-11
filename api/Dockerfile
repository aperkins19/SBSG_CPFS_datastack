FROM python:3

LABEL Author="Alex Perkins"
LABEL Email="a.j.p.perkins@sms.ed.ac.uk"
LABEL Version="0.1"


RUN mkdir /api
WORKDIR /api
ADD requirements.txt /api/
RUN pip install -r requirements.txt
ADD . /api/

EXPOSE 4000

CMD ["python","./main.py"]
