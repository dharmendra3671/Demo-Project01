import os 
import datetime
import glob
import zipfile
path = 'D:\Test'
count=0
count1=0
file=[]
for files in os.listdir(path):
    count+=1
    file.append(files)

print(os.path.join(path),f" \n List of Files in Current Directory are : {file}\n The no of files present in current Directory are : {count}")
older_files=[]
remove_list=[]
no_of_olddays=[]
today = datetime.datetime.today()
os.chdir(path)
for root,directories,files in os.walk(path,topdown=False):
   for name in files:
        t = os.stat(os.path.join(root, name))[8]
        filetime =abs(datetime.datetime.fromtimestamp(t) - today)
        
        if filetime.days>=7:
            count1+=1
            remove_list.append(name)
            no_of_olddays.append(filetime.days)
            os.remove(os.path.join(root, name))

  # print("The no of deleted files are: ",count1)
   print("List of Deleted Files older than Seven Days")
for x,y in zip(remove_list,no_of_olddays):
    print(f"Filename : {x} \t Filedays: {y}")          
for dirpath,dirnames,filenames in os.walk(path):
     print("Current Path",dirpath)
     print("current Directories",dirnames)
     print("List of recent Files less than Seven days are:",filenames) 


import os
from pathlib import Path
from zipfile import ZipFile
DOWNLOAD_DIR = Path('D:\Test')
ZIPPED_FILE_DIR = Path('D:\Test')

def get_list_of_all_folders(download_dir: Path):
    return [f for f in download_dir.iterdir() if download_dir.is_dir()]
def zip_files():
    folder_list = get_list_of_all_folders(DOWNLOAD_DIR)
    with ZipFile(ZIPPED_FILE_DIR / "Test1.zip", "w") as zip:
        for folder in folder_list:
            zip.write(folder)



zip_files()


