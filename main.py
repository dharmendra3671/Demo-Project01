import sys
from posnegint import *
limit=int(input("Enter limit "))
num=[]
pos_num = []
neg_num = []
print("Enter number to find list of positive and negative number.")
for i in range(limit):
    ele=int(input())
    num.append(ele)
ch=0
while ch!=3:
    print("Enter your choice \n1. To find Duplicate data \n 2. To find Unique data\n 3. EXIT")
    ch=int(input())
    if ch==1:
        duplicatedata(num,pos_num,neg_num)

    elif ch==2:
        uniquedata(num,pos_num,neg_num)
         
    else:
        sys.exit(0)
