n=int(input("Enter the limit:"))
a,b=0,1
count=0
if n<=0:
  print("Enter a number greater than 0")
elif n==1:
  print("Fibonacci series upto",n,"term:")
  print(a)
else:
  print("Fibonacci series upto",n,"terms:")
  while count<n:
    print(a)
    c=a+b
    a=b
    b=c
    count+=1
