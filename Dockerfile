FROM gorialis/alpine-rewrite-extras

WORKDIR /app

RUN apt update && \
    apt-get install -y texlive-full

COPY . .

CMD ["./run-owl.sh"]