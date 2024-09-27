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
        }

        stage('Get Command') {
            steps {
                script {
                    // Initialize pytestCommand
                    def pytestCommand = "pytest --disable-warnings"

                    // Append marker to the command if it's provided
                    if (params.marker?.trim()) {
                        pytestCommand += " -m ${params.marker}"
                    }

                    // Print the constructed command
                    echo "Running command: ${pytestCommand}"
                }
            }
        }
    }
}
