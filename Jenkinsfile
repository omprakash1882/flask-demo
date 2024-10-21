pipeline {
    agent any

    environment {
        DOCKERHUB_CREDENTIALS = credentials('dockerhub-credentials-id')
    }

    stages {
        stage('Checkout') {
            steps {
                git branch: 'main', url: 'https://github.com/omprakash1882/flask-demo.git'
            }
        }
        stage('Build docker image') {
            steps {  
                sh 'docker build -t omprakashkami/flask-demo:latest .'
            }
        }
        stage('login to dockerhub') {
            steps{
                sh 'echo $DOCKERHUB_CREDENTIALS_PSW | docker login -u $DOCKERHUB_CREDENTIALS_USR --password-stdin'
            }
        }
        stage('push image') {
            steps{
                sh 'docker push omprakashkami/flask-demo:latest'
            }
        }
    }
    post {
        always {
            sh 'docker logout'
        }
    }
}
