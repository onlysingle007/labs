lst = [] 
n = int(input("Enter number of elements : ")) 
for i in range(0, n): 
    ele = int(input()) 
  
    lst.append(ele)
      
print(lst)
sum=0 
for i in range(0,n):
    sum+=lst[i]

print("Sum = " + str(sum) )