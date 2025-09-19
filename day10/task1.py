def list_to_dict(nums):
    d = {}
    for num in nums:
        d[num] = num**3
    return d

numbers = [1, 2, 3, 4]
print(list_to_dict(numbers))
