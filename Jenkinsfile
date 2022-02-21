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

        stage ('Server..'){
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
                 serverId:"Artifactory server",
                  spec: '''{
                   "files": [
                      {
                      "pattern": "*.war",
                      "target": "libs--logic-ops-libs-snapshot-local"
                      }
                            ]
                           }''',
                           buildName: 'pipeline'
                        )
            }
        }
        stage ('Publish build info..') {
            steps {
                rtPublishBuildInfo (
                    serverId: "Artifactory server"
                )
            }
        }
    }
}       
