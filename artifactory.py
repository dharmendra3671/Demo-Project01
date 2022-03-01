from artifactory import ArtifactoryPath
path = ArtifactoryPath('http://127.0.0.1:8082/artifactory',
    auth=('admin', 'Kumar@6805'))
path.touch()

path.mkdir('Zipfile_Artifactory')

path.deploy_file('D:\\Test\\*.zip')
                
