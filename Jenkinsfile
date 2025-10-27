pipeline {
    agent {
        node {
            label "Chris"
        }
    }

    environment {
        IMAGE_NAME = 'hello-app'
        CONTAINER_NAME = 'hello-app'
        APP_PORT = '8000'
    }

    stages {
        stage('Checkout') {
            steps {
                echo 'Cloning repository...'
                git branch: 'main', url: 'https://github.com/notSkeletron/devopsproject.git'
            }
        }

        stage('Build Docker Image') {
            steps {
                echo 'Building Docker image...'
                script {
                    docker.build("${IMAGE_NAME}")
                }
            }
        }

        stage('Run App Container') {
            steps {
                echo 'Running the app container...'
                script {
                    // Stop old container if exists
                    sh '''
                    docker stop ${CONTAINER_NAME} || true
                    docker rm ${CONTAINER_NAME} || true
                    '''

                    // Run new container on port 8000
                    sh '''
                    docker run -d \
                        --name ${CONTAINER_NAME} \
                        -p ${APP_PORT}:8000 \
                        ${IMAGE_NAME}
                    '''
                }
            }
        }
    }

    post {
        success {
            echo "✅ Build and container run successfully!"
            echo "🌐 Access your app at: http://localhost:${APP_PORT}"
        }
        failure {
            echo "❌ Build or container run failed."
        }
    }
}