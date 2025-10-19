# # students = {"A": 85, "B": 92, "C": 78, "D": 95}
# Group Names by First Letter
# Example: ["Alice", "Bob", "Charlie", "David", "Bella"] →
# {‘A’: [‘Alice’], ‘B’: [‘Bob’, ‘Bella’], ‘C’: [‘Charlie’], ‘D’: [‘David’]
def grouping(Example):
    dic={}
    for exm in Example:
        letter=exm[0].upper()
        if letter not in dic:
            
            dic[letter]=[exm]
        else:
            dic[letter].append(exm)
    return dic
Example= ["Alice", "Bob", "Charlie", "David", "Bella"]
result=grouping(Example)
print(result)
