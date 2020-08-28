#!/bin/bash
sudo chmod 666 /var/run/docker.sock

docker-compose down --rmi all
docker-compose build
docker login
docker-compose push
