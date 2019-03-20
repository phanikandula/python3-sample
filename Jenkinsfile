pipeline {
  agent {
    docker {
      image 'python:3'
    }

  }
  stages {
    stage('Install') {
      steps {
        echo 'Installing..'
        sh 'make install'
      }
    }
    stage('Lint') {
      steps {
        echo 'Linting..'
        sh 'make lint'
      }
    }
    stage('Test') {
      steps {
        echo 'Testing..'
        sh 'make test'
      }
    }
    stage('Deploy') {
      steps {
        echo 'Deploying....'
      }
    }
  }
}