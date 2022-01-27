import os 
import datetime
import glob
path = 'D:\Demo-Project01\Source\Test'
today = datetime.datetime.today()
os.chdir(path)
print("List of files in the current Directory: ")
for root,directories,files in os.walk(path,topdown=False):
  print("Files:",files)
 #   for name in files:
#         t = os.stat(os.path.join(root, name))[8] 
#         filetime = datetime.datetime.fromtimestamp(t) - today
        
#         if filetime.days <= -7:
#             print(os.path.join(root, name), filetime.days)
#             os.remove(os.path.join(root, name))
    
