#!/bin/bash

while true; do
    git pull;
    python Main.py || exit 1;
done
