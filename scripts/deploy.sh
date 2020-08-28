#!/bin/bash
ssh manager << EOF
cd SFIA_Project_Week_9/
export SECRET_KEY=${SECRET_KEY} 
export DATABASE_URI=${DATABASE_URI} 
pwd
whoami
# scp /home/jason/SFIA_Project_Week_9 username@a:/path/to/destination
docker stack deploy --compose-file docker-compose.yaml sfia2
EOF