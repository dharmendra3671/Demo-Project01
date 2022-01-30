import os
import time
#from pathlib import Path
import zipfile

dir_name = 'D:\Demo-Project01\Source\Test'

list_of_files = filter( lambda x: os.path.isfile(os.path.join(dir_name, x)),
                        os.listdir(dir_name) )

list_of_files = sorted( list_of_files,
                        key = lambda x: os.path.getmtime(os.path.join(dir_name, x)))

for file in list_of_files[0:-5]:
    os.remove(os.path.join(dir_name,file))
list_of_files.reverse()
print("The Update Files are:")
for file_name in list_of_files[:5]:
    file_path = os.path.join(dir_name, file_name)
    timestamp_str = time.strftime('%d/%m/%Y :: %H:%M:%S',
                                time.gmtime(os.path.getmtime(file_path)))
    print(timestamp_str, ' -->', file_name)


def prepare_zip(dir_name):
    new_file = dir_name + '.zip'
    
    zip = zipfile.ZipFile(new_file, 'w', zipfile.ZIP_DEFLATED)
    
    for dir_name, dir_names, files in os.walk(dir_name):
        f_path = dir_name.replace(dir_name, '')
        f_path = f_path and f_path + os.sep
        
        for file in files:
            zip.write(os.path.join(dir_name, file), f_path + file)
    zip.close()
    print("File Created successfully..")
    return new_file


prepare_zip(dir_name)
