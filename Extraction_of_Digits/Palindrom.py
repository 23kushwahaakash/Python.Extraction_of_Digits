#PALINDROME
n=int(input("Enter the number: "))
num=n
rev=0
while num>0:
    rev=rev*10+num%10
    num=num//10
if rev==n:
    print("Palinderome")
else:
    print("Not a palindrome")