pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                git branch: 'master', url: 'https://github.com/kavtara1/JNKSPT.git'
            }
        }

        stage('Install Python and Pip') {
            steps {
                bat '''
                python3 --version
                pip --version
                '''
            }
        }

        stage('Install Dependencies') {
            steps {
                bat 'pip install -r requirements.txt'
            }
        }

        stage('Run Tests') {
            steps {
                bat 'pytest --maxfail=1 --disable-warnings'
            }
        }
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
