n=141
k=n
rev=0
while(n>0):
     rem=n%10
     rev=rev+(rem*rem*rem)
     n=n//10
if(n==0):
    print("armstrong")
else:
    print("not a armstrong")
