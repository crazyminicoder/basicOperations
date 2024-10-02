# insert
queue = []
queue.append(10)
queue.append(15)
queue.append(20)
queue.append(25)

print(queue)

# FIFO
# pop
print(queue.pop(0))
print(queue)

# pop last
print(queue.pop())
print(queue)

# peek first
print(queue[0])

# peek last
print(queue[-1])
