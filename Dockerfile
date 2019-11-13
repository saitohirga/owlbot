FROM gorialis/discord.py:3.8.0-buster-master-extras

WORKDIR /app

RUN sudo pip3 uninstall youtube-dl -y && \
 sudo pip3 install markovify>=0.7.0 youtube-dl psutil>=5.4.0 matplotlib>=3.1.0  requests>=2.22.0 aiohttp && \
 sudo apt-get update && \
 sudo apt-get install units -y

COPY . .

CMD ["./run-owl.sh"]
