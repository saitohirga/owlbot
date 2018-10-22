FROM gorialis/discord.py:3.7-rewrite-extras

WORKDIR /app

RUN apt update && \
    apt-get install -y texlive-full && sudo curl -L https://yt-dl.org/downloads/latest/youtube-dl -o \
    /usr/local/bin/youtube-dl && sudo chmod a+rx /usr/local/bin/youtube-dl

COPY . .

CMD ["./run-owl.sh"]