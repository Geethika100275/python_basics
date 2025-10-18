words = ["apple", "banana", "apricot", "blueberry", "avocado"]

count = {}
for w in words:
    first = w[0]
    count[first] = count.get(first, 0) + 1

print(count)
