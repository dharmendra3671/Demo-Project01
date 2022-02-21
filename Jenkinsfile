pipeline {
    agent any
        tools {
            maven "Maven"
                }
        stages {
        stage ('Python') {
            steps {
                bat 'PythonwithJson.py'
            }
        }

        stage ('Server'){
            steps {
                rtServer (
                    id: "Artifactory server",
                    url: 'http://127.0.0.1:8082/artifactory',
                    username: 'admin',
                    password: 'Kumar@6805',
                    bypassProxy: true,
                    timeout: 300
                        )

            }
        }
        stage ('Upload'){
            steps{
                rtUplode (
                 serverId:"Artifactory",
                  spec: '''{
                   "files": [
                      {
                      "pattern": "*.zip",
                      "target": "Zipfile_artifact"
                      }
                            ]
                           }''',
                           buildName: 'pipeline',
                           buildNumber: '29',
                        )
            }
        }
        stage ('Publish build info..') {
            steps {
                rtPublishBuildInfo (
                    serverId: "Artifactory"
                )
            }
        }
    }
}       
