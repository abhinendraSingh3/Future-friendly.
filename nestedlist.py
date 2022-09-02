#this is one of the question from hackerrank
n=int(input())
res=[]
grade=[]
for x in range(n):
    name=input()
    marks=float(input())
    res.append([name,marks])
    grade.append(marks)
grade=sorted(set(grade)) #calculation of unique numbers
m=grade[1] #2nd lowest
name=[]
for val in res:
    if m==val[1]:
        name.append(val[0])
name.sort()
for nm in name:
    print(nm)
    
