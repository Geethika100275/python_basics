# Convert a list of tuples into a dictionary.
# Example: [("a", 1), ("b", 2)] → {"a": 1, "b": 2}

def tupletodic(tuples):
    dic={}
    for tuple in tuples:
        dic[tuple[0]]=tuple[1]
    return dic
tuples=[("a", 1), ("b", 2)]
result=tupletodic(tuples)
print(result)
        
