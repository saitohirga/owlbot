#!/bin/bash

sudo git pull
sudo docker stop owl
sudo docker rm owl
sudo docker build -t owl .
sudo docker run -d --name owl owl