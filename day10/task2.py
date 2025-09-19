def common_elements(list1, list2):
    result = []
    for item in list1:
        if item in list2 and item not in result:
            result.append(item)
    return result

a = list(map(int, input("Enter first list of numbers (space separated): ").split()))
b = list(map(int, input("Enter second list of numbers (space separated): ").split()))

print("Common elements:", common_elements(a, b))
