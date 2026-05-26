##########################
## Build env
##########################

FROM python:3.10-bullseye AS BUILD

ENV DEBIAN_FRONTEND noninteractive

RUN apt-get update
#RUN apt-get upgrade -y
RUN apt-get install -y --no-install-recommends \
    ca-certificates pkg-config make \
    libssl-dev libffi-dev libpq-dev
    
COPY ./certificados-combinados.pem /usr/local/share/ca-certificates/certificados-combinados.pem
RUN update-ca-certificates

# Configurar pip para usar el proxy y el certificado
RUN mkdir -p /root/.pip && \
    echo "[global]" > /root/.pip/pip.conf && \
    echo "proxy = http://USUARIO:CONTRASEÑA@proxy.org:8080" >> /root/.pip/pip.conf && \
    echo "cert = /usr/local/share/ca-certificates/certificados-combinados.pem" >> /root/.pip/pip.conf && \
    echo "remote_read_timeout_secs = 180.0" >> /root/.pip/pip.conf && \
    echo "timeout = 100" >> /root/.pip/pip.conf

# python packages
RUN pip install --upgrade pip --trusted-host pypi.org --trusted-host files.pythonhosted.org --proxy http://USUARIO:CONTRASEÑA@proxy.org:8080
COPY requirements.txt /tmp/requirements.txt
RUN pip install -r /tmp/requirements.txt


##########################
## Final image
##########################
FROM python:3.10-bullseye

LABEL maintainer "CRG System Developers"
LABEL org.label-schema.schema-version="2.0"
LABEL org.label-schema.vcs-url="https://github.com/EGA-archive/beacon-2.x/"

# Too much ?
COPY --from=BUILD /usr/local/bin      /usr/local/bin
COPY --from=BUILD /usr/local/lib      /usr/local/lib

RUN apt-get update && \
    apt update && apt install -y openssh-client sshpass && \
    apt-get install -y --no-install-recommends \
    nginx \
    && \
    rm -rf /var/lib/apt/lists/* /etc/apt/sources.list.d/nginx.list && \
    apt-get purge -y --auto-remove


COPY . .

WORKDIR .
