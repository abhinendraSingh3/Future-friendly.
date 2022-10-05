r=int(input("Enter the number of rows "))
c=int(input("Enter the number of colomns "))
v1=[]
for _ in range(r):
    vo=[]
    for __ in range(c):
        co=int(input())
        vo.append(co)
    v1.append(vo)

for _ in range(r):
    for _ in range (c):
        print(v1[_][__],end=" ")
    print()        