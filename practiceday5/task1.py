def target_sum(numbers):
    uniq_list=[]
    for i in range (0,len(numbers)):
        for j in range  (1, len(numbers)):
            if numbers[i]+numbers[j]==target:
                uniq_list.append((numbers[i],numbers[j]))
    return uniq_list
numbers= [2, 4, 3, 5, 7, 8, -1]
target=7
result=target_sum(numbers)
print(result)
