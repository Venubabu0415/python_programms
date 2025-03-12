var=int(input("enter fibonacci series:"))
a=0
b=1
print("fibonacci series:",a,b)
for i in range(var-2):
    d=a+b
    a=b
    b=d
    print(d,end=" ")    