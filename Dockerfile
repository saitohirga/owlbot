FROM gorialis/discord.py:3.6.6-alpine-rewrite-extras

WORKDIR /app

RUN apt update && \
    apt-get install -y texlive-full \
    > /dev/null && \
    rm -rf /var/lib/apt/lists/*

COPY . .

CMD ["python", "Main.py"]
