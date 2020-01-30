n = int(input("Enter a number to find its factorial.\n"))
fact=n
if(n>0):
    while((n-1)!=0):
        fact=fact*(n-1)
        n=n-1
else:
    fact=1

print(fact)