a=int(input("Input a number"))
s=0
o=a
while(a>0):
    b=a%10
    c=b**3
    s=s+c
    a=a//10  
if o==s:
   print("Armstrong no.")
else:
    print("Not an Armstrong no.")
