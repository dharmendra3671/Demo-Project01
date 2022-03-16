# Creating user define Exception Class
class MyException(Exception):
    def __init__(self,arg):
       # Error message thrown is saved in msg
        self.msg=arg
#function defined to get duplicate data.
def duplicatedata(num,pos_num,neg_num):
    # Exception Handeling.
    for ele in num:
        try:
            if ele > 0:
                pos_num.append(ele)
                with open('positive.txt', 'w') as f:
                    for pos in pos_num:
                        f.write(str(pos) + '\n')

            elif ele==0:
                raise MyException(" 0  is neither postive nor negative number.")
            else:
               neg_num.append(ele)
               with open('negative.txt', 'w') as f:
                   for neg in neg_num:
                       f.write(str(neg) + '\n')
                   
        except MyException as me:
            print(me)
        finally:
           f.close()
        
# Function define to get unique data.                  
def uniquedata(num,pos_num,neg_num):
    pos_num=set(pos_num)
    neg_num=set(neg_num)
    
    for ele in num:
        try:
            if ele > 0:
                pos_num.add(ele)
                with open('positive.txt', 'w') as f:
                    for pos in pos_num:
                        f.write(str(pos) + '\n')

            elif ele==0:
                raise MyException("0 is neither postive nor negative number.")
            else:
               neg_num.add(ele)
               with open('negative.txt', 'w') as f:
                   for neg in neg_num:
                       f.write(str(neg) + '\n')
                       
        except MyException as me:
            print(me)
        finally:
            f.close()
