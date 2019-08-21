FROM gorialis/discord.py:3.8.0b2-master-extras

WORKDIR /app

RUN sudo pip3 uninstall youtube-dl -y && \
 sudo pip3 install markovify youtube-dl && \
 sudo apt-get update && \
 sudo apt-get install units -y

COPY . .

CMD ["./run-owl.sh"]
