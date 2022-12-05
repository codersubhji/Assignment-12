#2. Write a python script to check whether a given number is Prime or not
num=int(input("Enter any number to check whether a number is prime or not...:"))
if(num==1):
    print("Sorry it not a prime number")    
n=2  
while(num>=n):
    if(num==2):
        print("Yes it is a prime number " )
        break 
    elif(num%n==0)or(num%num!=0):
       print("Sorry it not a prime number")
       n+=1 
       break
    
    else:
       print("Yes it is a prime number ")
       break