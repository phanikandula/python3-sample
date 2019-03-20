pipeline {
  agent {
    docker {
      image 'python:3'
    }

  }
  stages {
    stage('Install') {
      steps {
        echo 'Install dep'
      }
    }
    stage('Lint') {
      steps {
        echo 'Linting'
      }
    }
    stage('Test') {
      steps {
        echo 'Testing'
      }
    }
  }
}