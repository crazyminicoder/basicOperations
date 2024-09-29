ml = []

# append
ml.append(5)
ml.append(3)
print(ml)

# insert inserts 7 at position 1
ml.insert(1, 7)
print(ml)

# remove it removes the first occurance
ml.remove(7)
print(ml)

ml.append(7)
ml.insert(1, 7)

print(ml)
ml.remove(7)

print(ml)

# extend iterable
ml.extend([10, 2, 8, 6])
print(ml)

# pop/ pop([i]) i = position
print(ml.pop())
print(ml.pop(2))
print(ml)

# search and count operations
# index index(x)/index(x, start, end)
print(ml.index(10))
print(ml.index(10, 1, 3))

# count
ml.extend([10, 5, 10, 9, 10, 68])
print(ml)
print(ml.count(10))

# Sorting and Reversing
ml.sort()
print(ml)
ml.sort(reverse=True)
print(ml)
ml.sort(key=lambda x: x//2)
print(ml)
ml.reverse()
print(ml)
