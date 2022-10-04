def largestNumber(arr,n):
    maxVal=arr[0]
    for val in range(1,n):
        if maxVal<arr[val]:
            maxVal=arr[val]
    return maxVal        

n=int(input("Enter the total Number of elements you want to enter"))
arr=[]
print("Enter the Elements")
for val in range(n):
    number=int(input())
    arr.append(number)
maxVal=largestNumber(arr,n)    
print("the largest number is",maxVal)