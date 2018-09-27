#!/bin/bash

sudo git pull
sudo docker stop ob
sudo docker rm ob
sudo docker build -t ob .
sudo docker run -d --name ob ob