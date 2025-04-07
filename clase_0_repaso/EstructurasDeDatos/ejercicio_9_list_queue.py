from collections import deque

queue = deque(['Juan', 'Maria', 'Alberto'])
print(queue)

queue.append('Rosa')
print(queue)

queue.append('José')
print(queue)

print(queue.popleft())

print(queue.popleft())

print(queue)