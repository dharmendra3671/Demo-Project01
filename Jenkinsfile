pipeline {
    agent any

    stages {
        stage('Python File') {
            steps {
                bat 'Pythonwithjason.py'
            }
        }
        stage('Test') {
            steps {
                echo 'Testing'
            }
        }
        stage('Release') {
            steps {
                echo 'Releasing'
            }
        }
    }
}

