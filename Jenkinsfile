pipeline {
    agent any
        stages {
        stage ('Python') {
            steps {
                bat 'PythonwithJson.py'
            }
        }
        stage ('Upload'){
            steps {
                bat 'zipartjf.py'
            }
        }
    }
}  
