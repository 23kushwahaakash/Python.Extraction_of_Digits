# COUNTING DIGITS
n=int(input("Enter the number: "))
num=n
digit=0
while num>0:
    digit+=1
    num=num//10
print("No. of digits: ",digit)