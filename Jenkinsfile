pipeline {
    agent any

    stages {
        stage('Python') {
            steps {
                bat 'python demo.py'
            }
        }
        stage('Build') {
            steps {
                bat "hello.bat"
            }
        }
        stage('Deploy') {
            steps {
                echo 'Deploying'
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

