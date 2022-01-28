import os 
import datetime
path = 'D:\Demo-Project01\Source\Test'
count=0
count1=0
file=[]
for files in os.listdir(path):
    count+=1
    file.append(files)
print(os.path.join(path),f" \n List of Files in Current Directory are : {file}\n The no of files present in current Directory are : {count}")
#older_files=[]
#remove_list=[]
#no_of_olddays=[]
today = datetime.datetime.today()
os.chdir(path)
for root,directories,files in os.walk(path,topdown=False):
   for name in files:
        t = os.stat(os.path.join(root, name))[8]
        filetime =abs(datetime.datetime.fromtimestamp(t) - today)
        
        if filetime.days>=7:
            count1+=1
            print("The no of old files are : {count1}",os.path.join(root, name), filetime.days)
            os.remove(os.path.join(root, name))
            
for dirpath,filenames in os.walk(path):
     print("Current Path",dirpath)
     print("The Updated Files are:",filenames)  
