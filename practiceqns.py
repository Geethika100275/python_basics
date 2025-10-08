def frequency(sentence):
    dic = {}
    words=sentence.split()
    for word in words:
        
            
            
        
        
            dic[word]=dic.get(word,0)+1
    return dic  
sentence = "Elephant is a big Animal!"
result=(frequency(sentence))
print(result) 
