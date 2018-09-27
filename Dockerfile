FROM gorialis/discord.py:3.6.6-alpine-rewrite-extras

WORKDIR /app

COPY . .

CMD ["python", "Main.py"]
