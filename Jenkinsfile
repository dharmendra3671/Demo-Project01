pipeline {
    agent any

    stages {
        stage('Python File') {
            steps {
                bat 'test.py'
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

