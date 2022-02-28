import os
import time
from pathlib import Path
from zipfile import ZipFile

dir_name = 'D:\Test

list_of_files = filter( lambda x: os.path.isfile(os.path.join(dir_name, x)),
                        os.listdir(dir_name) )

list_of_files = sorted( list_of_files,
                        key = lambda x: os.path.getmtime(os.path.join(dir_name, x)))

for file in list_of_files[5:]:
    os.remove(os.path.join(dir_name,file))
    

print("The Update Files are:")
for file_name in list_of_files[:5]:
    file_path = os.path.join(dir_name, file_name)
    timestamp_str = time.strftime('%m/%d/%Y :: %H:%M:%S',
                                time.gmtime(os.path.getmtime(file_path)))
    print(timestamp_str, ' -->', file_name)

PROjECT_DIR = Path(dir_name)

def get_list_of_all_folders(project_dir: Path):
    return [f for f in project_dir.iterdir() if project_dir.is_dir()]
def zip_files():
    folder_list = get_list_of_all_folders(PROjECT_DIR)
    with ZipFile(PROjECT_DIR/ "Test1.zip", "w") as zip:
        for folder in folder_list:
          zip.write(folder)

zip_files()



