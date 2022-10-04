import array as arr

alpha=arr.array('i',[1,3,9,2,3])
count=0
for values in alpha:
    if values==3:
     count=count+1
print(count)