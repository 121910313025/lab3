#write a python program to count the number of vowels in a file
#121910313025
f=open(input("enter a file name:"))
data=f.read()
count=0
data.lower()
for i in data:
    if (i=='a' or i=='e' or i=='i' or i=='o'or i=='u'):
        count=count+1
print(count)
f.close()
