d1={'Laptop':80000,'Smartphone':20000,'Television':50000}
e=max(d1.values())
for k,v in d1.items():
    if v==e:
        print(k)
