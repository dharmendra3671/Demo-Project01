pipeline {
    agent any

    stages {
        stage('Python File') {
            steps {
                bat 'demo.py'
            }
        }
        stage('Batch File') {
            steps {
                bat "hello.bat"
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

