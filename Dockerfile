FROM centos:latest

LABEL name='impulse'
LABEL version='0.1'
LABEL description='An endpoint checking service'
LABEL org.ctrlaltdev.vendor='ctrlaltdev'

RUN yum upgrade -y
RUN yum install crontabs -y

ADD db/ hosts/ impulse.py /impulse/

WORKDIR /impulse

RUN echo "* * * * * /impulse/impulse.py >> /dev/null" | crontab -