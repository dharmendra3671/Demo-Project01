pipeline {
    agent any
        tools {
            maven "3.8.4"
                }

    stages {
         stage('Git CheckOut') {
            steps {
                git branch: 'main', credentialsId: 'dharmendra3671 Indro@6805', url: 'https://github.com/dharmendra3671/Demo-Project01/edit/main/Jenkinsfile'
            }
        }
        stage('Python File') {
            steps {
                bat 'Test.py'
            }
        }
        stage('Clean and Install') {
            steps {
                bat 'mvn clean install'
            }
        }
        stage('Package') {
            steps {
                bat 'mvn package'
            }
        }
        stage('Server') {
            steps {
                rtServer (
                    id: "Artifactory",
                    url: 'http://127.0.0.1:8082/artifactory',
                    username: 'admin',
                     password: 'Indro@6805',
                     bypassProxy: true,
                      timeout: 300
                           )
            }
        }
        stage('Upload') {
            steps {
                rtUpload (
                    ServerId: "Artifactory",
                    spec: '''{
                     "files": [
                        {
                        'pattern': '*.war',
                        'target': 'logic-ops-lab-libs-snapshot-local'
                        }
                            ]
                           }''',
                        )
           }
        }
        stage('Publish build info') {
            steps {
                rtPublishBuildInfo (
                    serverId:'Artifactory'
                )
            }
        }
    }
}

