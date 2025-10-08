def average(students):
    dic={}
    for name , marks in students.items():
        
        
        avg=sum(marks)/len(marks)
        dic[name]=avg
    return dic
students = {'Alice': [85, 90, 95], 'Bob': [70, 75, 80]}
result = average(students)
print(result)
