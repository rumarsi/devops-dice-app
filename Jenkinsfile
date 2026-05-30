pipeline {
    agent any

    environment {
        IMAGE_NAME = 'rumarsi/devops-dice-app'
        IMAGE_TAG = 'latest'
        CONTAINER_NAME = 'devops-dice-app-test'
        DOCKERHUB_CREDENTIALS = 'dockerhub-credentials'
    }

    stages {
        stage('Limpieza del workspace') {
            steps {
                cleanWs()
            }
        }

        stage('Checkout del código') {
            steps {
                checkout scm
            }
        }

        stage('Construimos la imagen del contenedor') {
            steps {
                sh 'docker build -t ${IMAGE_NAME}:${IMAGE_TAG} .'
            }
        }

        stage('Probamos que se ejecuta correctamente') {
            steps {
                sh '''
                    docker rm -f ${CONTAINER_NAME} || true
                    docker run --name ${CONTAINER_NAME} ${IMAGE_NAME}:${IMAGE_TAG} > output.log
                    cat output.log
                    test -s output.log
                    docker rm -f ${CONTAINER_NAME} || true
                '''
            }
        }

        stage('Subimos la imagen a Docker Hub') {
            steps {
                script {
                    docker.withRegistry('', DOCKERHUB_CREDENTIALS) {
                        sh 'docker push ${IMAGE_NAME}:${IMAGE_TAG}'
                    }
                }
            }
        }
    }

    post {
        failure {
            echo 'El pipeline ha fallado.'
        }
    }
}
