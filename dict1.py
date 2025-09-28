def dictionary(students):
     students = ["Alice", "Bob", "alice", "ALICE", "bob", "Charlie"]
     dic={}
     for student in students:
         key=student.lower()
         dic[key] = dic.get(key,0)+1
         
         
         
     return dic
students = ["Alice", "Bob", "alice", "ALICE", "bob", "Charlie"]     
result=dictionary(students)
print(result)
