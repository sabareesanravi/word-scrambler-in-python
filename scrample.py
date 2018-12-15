import random
def fun(list1=[]):
    list2=[]
    for i in list1:
        if(len(i)<=3):
            list2.append(i)
        else:
            mid=i[1:-1]
            gg=list(mid)
            random.shuffle(gg)
            kk=''.join(gg)
            list2.append(i[0]+kk+i[-1])
    return list2

fp=open("christmas.txt",'r')
fp1=open("christmas1.txt",'w')
l=[]
m=[]
str1=fp.readlines()
for i in str1:
    l=i.split(' ')
    m=fun(l)
ff=' '.join(m)
fp1.write(ff)
fp.close()
fp1.close()
print("THE FILE SCRAMBLING IS DONE PLEASE CHECK THE FILE")
