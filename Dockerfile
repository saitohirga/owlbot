FROM gorialis/discord.py:3.7-rewrite-extras

WORKDIR /app

RUN apt update && apt-get install -y texlive-full

COPY . .

CMD ["sudo chmod +x run-owl.sh && ./run-owl.sh"]