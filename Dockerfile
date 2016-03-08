FROM python:3.4
ENV PYTHONBUFFERED 1
RUN mkdir /code
WORKDIR /code
ADD . /code
RUN pip install -r requirements/base.txt

