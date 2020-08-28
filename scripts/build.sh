#!/bin/bash
sudo docker-compose down --rmi all
sudo docker-compose build
sudo docker login
sudo docker-compose push