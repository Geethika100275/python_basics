def arr_move():
    
    j=0
    chocolate=[1,0,2,0,3,4]
    for i in range(len(chocolate)):
        if chocolate[i]!=0:
            chocolate[j]=chocolate[i]
            j+=1
            
    while j<(len(chocolate)):
            chocolate[j]=0
            j+=1
            
    return chocolate
print(arr_move())
