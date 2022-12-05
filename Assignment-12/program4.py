"""4. Write a python script to print all Prime numbers between two given numbers (both
values inclusive)"""
num1=int(input("Enter initial number....:")) 
num2=int(input("Enter last number.....:"))
for a in range(num1,num2+1):
    count=0
    r=a//2+1
    for i in range(2,r):
        if(a%i==0):
         count+=1
    if(count<=0):
        print(a,end=" ")  