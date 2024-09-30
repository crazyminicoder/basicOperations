# Stack in list:
# push
stack = []
stack.append(5)
stack.append(21)
stack.append(12)

print(stack)

# pop
print(stack.pop())

# peek
top = stack[-1]
print(top)
print(stack)

# isEmpty
if not stack:
    print('stack is empty')
else:
    print('not empty')
