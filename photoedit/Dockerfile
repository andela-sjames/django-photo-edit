FROM python:2.7.13
ENV PYTHONUNBUFFERED 1

RUN mkdir -p /photoedit/run_web.sh
WORKDIR /photoedit
ADD requirements.txt /photoedit/
ADD run_web.sh /photoedit/
RUN chmod u+x ./run_web.sh 
RUN pip install -r requirements.txt
# create unprivileged user
RUN adduser --disabled-password --gecos '' gentlefella
COPY . /photoedit/
ENTRYPOINT ["./run_web.sh"]
