FROM gorialis/discord.py:3.7.2-stretch-rewrite-extras

WORKDIR /app

COPY ./docker-entrypoint.sh /
ENTRYPOINT ["/docker-entrypoint.sh"]
CMD ["$@"]


COPY . .

CMD ["./run-owl.sh"]
