pipeline {
    agent any

    environment {
        DOCKERHUB_CREDENTIALS = credentials('dockerhub-credentials-id')
        //DOCKER_IMAGE = 'omprakashkami/flask-demo'
    }

    stages {
        stage('Checkout') {
            steps {
                git branch: 'main', url: 'https://github.com/omprakash1882/flask-demo.git'
            }
        }
        stage('Build docker image') {
            steps {  
                sh 'docker build -t omprakashkami/flaskapp:$BUILD_NUMBER .'
            }
        }
        stage('login to dockerhub') {
            steps{
                sh 'echo $DOCKERHUB_CREDENTIALS_PSW | docker login -u $DOCKERHUB_CREDENTIALS_USR --password-stdin'
            }
        }
        stage('push image') {
            steps{
                sh 'docker push omprakashkami/flaskapp:$BUILD_NUMBER'
            }
        }

        // stage('Build Docker Image') {
        //     steps {
        //         script {
        //             docker.build("${DOCKER_IMAGE}:${env.BUILD_ID}")
        //         }
        //     }
        // }

        // stage('Push Docker Image') {
        //     steps {
        //         script {
        //             docker.withRegistry('https://index.docker.io/v1/', DOCKERHUB_CREDENTIALS) {
        //                 docker.image("${DOCKER_IMAGE}:${env.BUILD_ID}").push()
        //             }
        //         }
        //     }
        // }
    }
}
