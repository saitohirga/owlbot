FROM gorialis/discord.py:3.6-rewrite-extras

WORKDIR /app

COPY . .

CMD ["python", "Main.py"]
