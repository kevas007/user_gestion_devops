pipeline {
  agent any

  environment {
    DOCKERHUB = credentials('docker-hub-creds')
    TAG       = env.BUILD_NUMBER
  }

  stages {
    stage('Checkout') {
      steps { checkout scm }
    }

    stage('Build & Test Backend') {
      dir('backend') {
        steps {
          sh 'pytest --maxfail=1 --disable-warnings -q'
          sh "docker build -t myorg/api:${TAG} ."
        }
      }
    }

    stage('Build Frontend') {
      dir('frontend') {
        steps {
          sh 'npm ci'
          sh 'npm run build'
          sh "docker build -t myorg/frontend:${TAG} ."
        }
      }
    }

    stage('Publish Images') {
      steps {
        script {
          docker.withRegistry('', 'docker-hub-creds') {
            sh "docker push myorg/api:${TAG}"
            sh "docker push myorg/frontend:${TAG}"
          }
        }
      }
    }

    stage('Deploy Docker Stack') {
      steps {
        sh 'docker-compose pull && docker-compose up -d'
      }
    }
  }

  post {
    always { cleanWs() }
  }
}
