x=input("Enter any string:")
y=x.split()
start=0
last=len(x)-1                                       
if(x==x[::-1]):
 print("The string is palindrome")
else:
 print("The string is not palindrome")
