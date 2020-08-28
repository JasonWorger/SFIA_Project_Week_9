#!/bin/bash
pwd
export TEST_SECRET_KEY=${TEST_SECRET_KEY} 
export TEST_DATABASE_URI=${TEST_DATABASE_URI} 
# test servcie1
cd ./service1
pip3 install -r requirements.txt
python3 -m pytest --cov application 
cd ..

# test servcie2
cd ./service2
python3 -m pytest --cov application
cd ..

# test servcie3
cd ./service3
python3 -m pytest --cov application
cd ..

# test servcie4
cd ./service4
python3 -m pytest --cov application
cd ..