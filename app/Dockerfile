FROM ubuntu:latest

RUN apt-get update -y && \
    apt-get install -y python3 python-pip python-dev build-essential python3-distutils


RUN echo "LC_ALL=C.UTF-8" >> /etc/environment && \
    echo "LANG=C.UTF-8" >> /etc/environment 

ENV LC_ALL=C.UTF-8
ENV LANG=C.UTF-8

COPY . /app

ARG USER_ID=1001
ARG GROUP_ID=1001
ARG username

RUN groupadd -g ${GROUP_ID} ${username} && \
    useradd -l -u ${USER_ID} -g ${username} ${username} && \
    install -d -m 0755 -o ${username} -g ${username} /home/${username} && \
    chown -R ${USER_ID}:${GROUP_ID} /usr/local 
    
RUN chown -R ${username} /app

WORKDIR /app

RUN pip install pipenv 

USER ${username} 

RUN pipenv install 

CMD [ "pipenv", "run", "flask", "run", "--host=0.0.0.0" ]
