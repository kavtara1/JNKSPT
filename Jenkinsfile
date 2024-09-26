pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                // Clone your repository
                git url: 'https://github.com/kavtara1/JNKSPT.git'
            }
        }

        stage('Install Dependencies') {
            steps {
                // Install Python and pytest dependencies
                sh 'cd JNKSPT'
                sh 'pip install -r requirements.txt'
            }
        }

        stage('Run Tests') {
            steps {
                // Run pytest and generate a JUnit report
                sh 'pytest --junitxml=reports/test-results.xml'
            }
        }
    }

    post {
        always {
            // Publish test results
            junit 'reports/test-results.xml'
        }
    }
}
