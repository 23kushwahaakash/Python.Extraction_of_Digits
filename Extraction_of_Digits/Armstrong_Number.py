# ARMSTRONG NUMBER
n=int(input("Enter the number: "))
num=n
digit=0
new=0
while num>0:
    digit+=1
    num=num//10
num=n
while num>0:
    new=new+(num%10)**digit
    num=num//10
if new==n:
    print("Armstrong Number")
else:
    print("Not an Armstrong Number")
