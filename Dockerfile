FROM gorialis/discord.py:3.7.2-stretch-rewrite-extras

WORKDIR /app

RUN sudo curl -L https://yt-dl.org/downloads/latest/youtube-dl -o /usr/local/bin/youtube-dl && \
 sudo chmod a+rx /usr/local/bin/youtube-dl && \
 sudo pip3 install feedparser markovify && \
 sudo apt-get update && \
 sudo apt-get install units -y && \
 wget https://www.eecis.udel.edu/~ntp/ntp_spool/ntp4/ntp-4.2/ntp-4.2.8p13.tar.gz && \
 tar zxvf ntp-4.2.8p13.tar.gz && \
 cd ntp-4.2.8p13 && \
 ./configure && \
 make && \
 sudo make install && \
 sudo ntpd


COPY . .

CMD ["./run-owl.sh"]
