pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                // Clone your repository
                git url: 'https://github.com/kavtara1/JNKSPT.git'
            }
        }

        stage('Setup Python Environment') {
            steps {
                // Install virtualenv if not already installed
                cd JNKSPT
                bat 'python --version'
                bat 'pip install virtualenv'

                // Create a virtual environment
                bat 'virtualenv venv'

                // Activate the virtual environment and install dependencies
                bat '''
                venv\\Scripts\\activate
                pip install -r requirements.txt
                '''
            }
        }

        stage('Run Tests') {
            steps {
                // Activate the virtual environment and run pytest
                bat '''
                venv\\Scripts\\activate
                pytest --junitxml=reports\\test-results.xml
                '''
            }
        }
    }

    post {
        always {
            // Publish test results
            junit 'reports/test-results.xml'
        }

        cleanup {
            // Clean up the virtual environment or any temporary files
            bat '''
            rmdir /S /Q venv
            '''
        }
    }
}
