# Given a list of words, create a dictionary that maps each word to its length.
# Example: ["cat", "apple", "dog"] → {"cat": 3, "apple": 5, "dog": 3}
def mapping(objects):
    dic = {}
    for obj in objects:
        
        dic[obj]=len(obj)
    return dic
objects = ["cat", "apple", "dog"]
result=mapping(objects)
print(result)
