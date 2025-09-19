def group_by_length(words):
    d = {}
    for word in words:
        length = len(word)
        if length in d:
            d[length].append(word)
        else:
            d[length] = [word]
    return d
words = input("Enter words separated by spaces: ").split()
print("Grouped by length:", group_by_length(words))
