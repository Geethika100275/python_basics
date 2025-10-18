nums = [2, 7, 11, 15]
target = 9



seen = {}
for num in nums:
    diff = target - num
    if diff in seen:
        print((diff, num))
        break
    seen[num] = True
