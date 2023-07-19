FROM postgres:15.1-alpine

LABEL author="Mark Marton"
LABEL description="PostgreSQL database for the messagecollector"
LABEL version="1.0"

COPY ./init.sql /docker-entrypoint-initdb.d/

