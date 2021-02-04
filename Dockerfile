FROM gorialis/discord.py:buster-master-extras

WORKDIR /app

RUN sudo pip3 uninstall youtube-dl -y && \
 sudo pip3 install markovify youtube-dl psutil matplotlib  requests aiohttp wolframalpha discord.py[voice] && \
 sudo apt-get update && \
 sudo apt-get install units ntp -y

COPY . .

CMD ["./run-owl.sh"]
