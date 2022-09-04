list=[]
n=int(input())
for x in range(n): #this shows the number of inputs user will give
  nl=input().split() #suppose user typed "insert 0 12" then split function will split the text into list type like['insert','0','12'] and will hence give indexing
  if nl[0]=="insert": #this shows if the index 0 is keyword insert then 
      list.insert(int(nl[1]),int(nl[2])) #it will insert 1st index value(of nl) as position(list) in insert function and 2nd value(of nl) as no. to be inserted at that position
  elif nl[0]=="print":
     print(list)
  elif nl[0]=="remove":
     list.remove(int(nl[1]))
  elif nl[0]=="append":
     list.append(int(nl[1]))
  elif nl[0]=="sort":
     list.sort()
  elif nl[0]=="pop":
     list.pop()
  else:
     list.reverse()
    
      
  