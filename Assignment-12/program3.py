#3. Write a python script to print all Prime numbers under 100
num=int(input("Give a nuumber....:")) 
for a in range(2,num+1):
    count=0
    r=a//2+1
    for i in range(2,r):
        if(a%i==0):
         count+=1
    if(count<=0):
        print(a,end=" ")        
            
    
