FROM gorialis/discord.py:alpine-rewrite-extras

WORKDIR /app

RUN apt update && apt-get install -y texlive-full

COPY . .

CMD ["chmod +x run-owl.sh && ./run-owl.sh"]