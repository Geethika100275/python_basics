def list_to_dict(nums):
    d = {}
    for num in nums:
        d[num] = num**3
    return d

numbers = list(map(int, input("Enter numbers separated by spaces: ").split()))
print("Dictionary of cubes:", list_to_dict(numbers))
