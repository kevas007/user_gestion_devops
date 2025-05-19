pipeline {
  agent any

  environment {
    // Credentials binding pour Docker Hub
    REGISTRY_CREDENTIALS = 'docker-hub-creds'
    // URL de Docker Hub (V1 pour compatibilité)
    REGISTRY_URL         = 'https://index.docker.io/v1/'
    TAG                  = env.BUILD_NUMBER
    IMAGE_API            = "myorg/api"
    IMAGE_FRONTEND       = "myorg/frontend"
  }

  stages {
    stage('Checkout') {
      steps {
        checkout scm
      }
    }

    stage('Build & Test Backend') {
      dir('backend') {
        steps {
          sh 'pytest --maxfail=1 --disable-warnings -q'
          sh "docker build -t ${IMAGE_API}:${TAG} ."
        }
      }
    }

    stage('Build Frontend') {
      dir('frontend') {
        steps {
          sh 'npm ci'
          sh 'npm run build'
          sh "docker build -t ${IMAGE_FRONTEND}:${TAG} ."
        }
      }
    }

    stage('Publish Images') {
      steps {
        script {
          // On se connecte au registre avec URL explicite et credentials
          docker.withRegistry("${REGISTRY_URL}", "${REGISTRY_CREDENTIALS}") {
            sh "docker push ${IMAGE_API}:${TAG}"
            sh "docker tag ${IMAGE_API}:${TAG} ${IMAGE_API}:latest"
            sh "docker push ${IMAGE_API}:latest"

            sh "docker push ${IMAGE_FRONTEND}:${TAG}"
            sh "docker tag ${IMAGE_FRONTEND}:${TAG} ${IMAGE_FRONTEND}:latest"
            sh "docker push ${IMAGE_FRONTEND}:latest"
          }
        }
      }
    }

    stage('Deploy Docker Stack') {
      steps {
        // Déploie vos images avec docker-compose
        sh '''
          docker-compose pull
          docker-compose up -d
        '''
      }
    }
  }

  post {
    always {
      // Nettoyage du workspace
      cleanWs()
    }
  }
}
