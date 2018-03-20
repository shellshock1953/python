pipeline {
  agent any

  environment {
    branch = 'some_branch'
  }

  stages {
    stage("Pre") {
        steps {
            echo "Running ${env.BUILD_ID} on ${env.JENKINS_URL} to build ${env.branch}"
        }
    }
    stage("Execute") {
      steps {
        sh "ls -l"
      }
    }
  }
}
