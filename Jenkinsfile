pipeline {

    agent any

    parameters {
        string(defaultValue: 'SIT', description: 'Select environment: SIT, DEV, QA', name: 'enviroment', trim: true)
    }

    stages {
        stage('Check Environment') {
            steps {
                script {
                    if (params.enviroment == "SIT") {
                        echo "Hello SIT"
                    } else {
                        echo "Other environment selected: ${params.enviroment}"
                    }
                }
            }
        }
    }
}
