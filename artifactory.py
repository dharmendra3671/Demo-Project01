import os
import glob

from artifactory import ArtifactoryPath
path = ArtifactoryPath('http://127.0.0.1:8082/artifactory/python',
    auth=('admin', 'Root@123'))
path.touch()

def filename():
    os.chdir(r'D:\Test\t1')
    for file in glob.glob("*.zip"):
        if os.path.exists(file):
            return file


path.deploy_file(filename())

                
