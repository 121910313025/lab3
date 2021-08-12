l=[1,2,3,4]
sum=0
for i in l:
    sum=sum+i
lst=[]
for i in l:
    if i != 0:
        lst.append(i)
        
k=sum*len(lst)
print(k)
