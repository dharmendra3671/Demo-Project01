import os 
import datetime
import glob
path = 'D:\Demo-Project01\Test'
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
           # print(os.path.join(root, name),"No of days of Created File :", filetime.days)
            os.remove(os.path.join(root, name))

   print("The no of deleted files are: ",count1)
   print("List of Delted Files older than Seven Days")
for x,y in zip(remove_list,no_of_olddays):
    print(f"Filename : {x} \t Filedays: {y}")          
for dirpath,dirnames,filenames in os.walk(path):
     print("Current Path",dirpath)
     print("current Directories",dirnames)
     print("The Most Recent Files are:",filenames) 
