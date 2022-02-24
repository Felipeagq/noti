FROM python:3.8

EXPOSE 5000

### MODIFICAR A PARTIR DE AQUI ### 
WORKDIR /usr/src/app

COPY ./requirements.txt requirements.txt

RUN pip3 install -r requirements.txt

COPY ./ ./ 

CMD [ "python3","entrypoint.py" ]