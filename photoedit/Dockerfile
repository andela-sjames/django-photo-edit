FROM python:2.7.13
RUN mkdir /photoedit
WORKDIR /photoedit
ADD requirements.txt /photoedit/
RUN pip install -r requirements.txt
COPY . /photoedit/
