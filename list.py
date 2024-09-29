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

# Membership
print(1 in ml)

# Concatenation and Repetition
ml2 = ml + [101, 15, 3]
print(ml2)

# repetition
ml3 = [1, 2, 3]
ml4 = ml3 * 2
print(ml4)

# Comprehension
squares = [x**2 for x in range(6)]
print(squares)


# popping 9 from ml but I dont know the position of 9
ml.pop(ml.index(9))
print(ml)
