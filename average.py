'''students={}
for val in range(3):
    name=input()
    marks=input()
    students[name]=marks
    marks=tuple(marks)

print(students)
n=(input(students.keys))
print()'''
 


if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split() #taking input and saving in name,line and changing line by*line  
        scores = list(map(float, line)) #making line contents in float and storing it in list of scores                                                                                      list
        student_marks[name] = scores #assigning dict key to values
    query_name = input()
    mrks=student_marks[query_name]
    #format(value,.nf) its a function to print average upto N numbers
    print (format(sum(mrks)/3,'.2f'))
