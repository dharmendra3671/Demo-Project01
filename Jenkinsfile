pipeline {
    agent any

    stages {
        stage('Python File') {
            steps {
                bat 'PythonwithJson.py'
            }
        }
        stage('Test') {
            steps {
                echo 'Testing1'
            }
        }
        stage('Release') {
            steps {
                echo 'Releasing'
            }
        }
    }
}

