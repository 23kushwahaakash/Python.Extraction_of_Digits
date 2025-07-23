# REVERSING A NUMBER
n=int(input("Enter the number: "))
m=n
newn=0
while m>0:
    newn=newn*10+m%10
    m=m//10
print(newn)