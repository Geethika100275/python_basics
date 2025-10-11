def words(objects):
    dic = {}
    for obj in objects:
        length=len(obj)
        if length in dic:
            
           dic[length].append(obj)
        else:
            dic[length]=[obj]
    return dic
objects = ["bat", "apple", "cat", "dog", "banana"] 
result = words(objects)
print(result)
