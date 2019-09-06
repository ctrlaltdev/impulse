FROM alpine:latest

LABEL name='impulse'
LABEL version='0.2'
LABEL description='An endpoint checking service'
LABEL org.ctrlaltdev.vendor='ctrlaltdev'

RUN set -x && apk --no-cache add python3

ADD db/ hosts/ impulse.py /impulse/

WORKDIR /impulse

VOLUME /impulse/hosts
VOLUME /impulse/db

RUN echo "* * * * * /impulse/impulse.py >> /dev/null" | crontab -

ENTRYPOINT [ "crond" ]