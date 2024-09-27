pipeline {
    agent any

    parameters {
      string defaultValue: 'SIT', description: 'select inviroment, SIT, DEV, QA', name: 'enviroment', trim: true
    }


    stages {
      stage{
      echo "params.enviroment"
      }

    post {
        always {
            junit '**/test-results.xml'
        }

        failure {
            echo 'Test failed!'
        }

        success {
            echo 'All tests passed!'
        }
    }
}
}