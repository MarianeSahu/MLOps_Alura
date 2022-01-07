# Execução prompt: docker build -f Dockerfile -t app-mlops --build-arg BASIC_AUTH_USERNAME_ARG=mariane --build-arg BASIC_AUTH_PASSWORD_ARG=senha .

FROM python:3.9-slim

# ambiente
WORKDIR /usr
ARG BASIC_AUTH_USERNAME_ARG
ARG BASIC_AUTH_PASSWORD_ARG

ENV BASIC_AUTH_USERNAME=$BASIC_AUTH_USERNAME_ARG
ENV BASIC_AUTH_PASSWORD=$BASIC_AUTH_PASSWORD_ARG

# bibliotecas
COPY ./requirements.txt /usr/requirements.txt
RUN pip3 install -r requirements.txt

# arquivos
COPY ./MLOps_main.py /usr/MLOps_main.py
COPY ./modelo_preco_casas.sav /usr/modelo_preco_casas.sav

ENTRYPOINT [ "python3" ]

CMD [ "MLOps_main.py" ]