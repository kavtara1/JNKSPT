pipeline {

    agent any

    parameters {
        string(defaultValue: 'SIT', description: 'Select environment: SIT, DEV, QA', name: 'enviroment', trim: true)
    }

    stages {
        stage('Print Environment') {
            steps {
                script {
                    echo "Selected environment: ${params.enviroment}"
                }
            }
        }
    }
}
