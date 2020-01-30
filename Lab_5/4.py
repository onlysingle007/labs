x = input("Enter a string.")
count=0
for i in range(0,int(len(x)/2)):
    if(x[i]==x[len(x)-i-1]):
        count=count+1
if(count==int(len(x)/2)):
    print("String is a palindrome.")
else:
    print("String is not a palindrome.")