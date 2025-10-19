def max_(students):
    dic={}
    for student , info in students.items():
        
        # maximum=students.get(max(students))
        
        dic["maximum"]=max(students)
    return dic
students = {"A": 85, "B": 92, "C": 78, "D": 95}
result=max_(students)
print(result)
