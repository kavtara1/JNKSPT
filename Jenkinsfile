pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                // Checkout the code from your Git repository
                git branch: 'master', url: 'https://github.com/kavtara1/JNKSPT.git'
            }
        }

        stage('Install Dependencies') {
            steps {
                // Assuming you have a requirements.txt to install dependencies
                bat 'pip install -r requirements.txt'
            }
        }

        stage('Run Tests') {
            steps {
                // Run pytest
                bat 'pytest --maxfail=1 --disable-warnings'
            }
        }
    }

    post {
        always {
            // Publish test results (JUnit format for Jenkins to parse)
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
