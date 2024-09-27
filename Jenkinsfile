pipeline {

    agent any

    parameters {
        string(defaultValue: 'SIT', description: 'Select environment: SIT, DEV, QA', name: 'enviroment', trim: true)
        string(defaultValue: '', description: 'Marker to run specific tests (e.g., smoke, regression)', name: 'marker', trim: true)

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
        stage("get command") {
            steps {
                script {
                    def pytestcommand = "pytest --disable-warnings"
                     if (params.marker?.trim()) {
                        pytestCommand += " -m ${params.marker}"
                        echo pytestCommand += " -m ${params.marker}"
                    }
                    else {

                     echo pytestCommand

                    }

                }
            }
          }
        }
    }
}
