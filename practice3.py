def even_odd(numbers):
    dic = {}
    for num in numbers:
        if num%2==0:
            dic["even"]=dic.get("even",0)+1
        else:
            dic["odd"]=dic.get("odd",0)+1
    return dic
numbers =[1, 2, 3, 4, 5, 6,7]
result=even_odd(numbers)
print(result)
