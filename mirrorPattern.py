n=int(input("Enter the number of stars to be printed"))
for i in range(n):
  print(""*(n-i-1)+"*"*(i+1))
  
  #OR
  
n = int(input().strip())
for i in range(n):
    for j in range(n-i-1):
         print(" ",end="")
    for j in range(i+1):
          print("#",end="")
    print()
