pipeline {
    agent any 
    stages{
        stage('Install Docker'){
            steps{
                sh './scripts/docker_install.sh'
            }        
        }
        stage('Test services'){
            steps{
                sh './scripts/test_services.sh'
            }
        }
        stage('Deploy services'){
            steps{
                sh './scripts/docker_deploy.sh'
            }
        }
    }
                   
}