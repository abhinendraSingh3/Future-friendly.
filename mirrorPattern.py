n=int(input("Enter the number of stars to be printed"))
for i in range(n):
  print(""*(n-i-1)+"*"*(i+1))
