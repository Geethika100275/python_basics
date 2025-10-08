def words(Example):
    dic = {}
    for words in Example:
        letter = words[0].lower()
        dic[letter]=dic.get(letter,0)+1
    return dic
Example =  ["apple", "ant", "ball", "bat", "banana"]
result = words(Example)
print(result)
