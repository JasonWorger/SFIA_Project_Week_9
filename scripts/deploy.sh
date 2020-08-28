#!/bin/bash
ssh manager << EOF
cd SFIA-PROJECT_2/
export SECRET_KEY=${SECRET_KEY} 
export DATABASE_URI=${DATABASE_URI} 
docker stack deploy --compose-file docker-compose.yaml sfia2
EOF