FROM daocloud.io/python:3.5

RUN mkdir -p /home/app 
WORKDIR /home/app 

ADD ./requirements.txt /home/app/requirements.txt 

RUN pip3 install --upgrade pip 
RUN pip3 install -r requirements.txt 

ADD . /home/app 
EXPOSE 80

CMD python app.py