FROM ubuntu:latest

RUN apt-get update && apt-get install -y cowsay fortune netcat-openbsd

COPY wisecow.sh /app/wisecow.sh

WORKDIR /app

RUN chmod +x wisecow.sh

EXPOSE 4499

CMD ["./wisecow.sh"]

ENV PATH="/usr/games:${PATH}"