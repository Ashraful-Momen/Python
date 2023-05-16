from collections import deque

queue = deque(['a', 'b', 'c'])

queue.popleft()
queue.popleft()
queue.popleft()

if not queue:
    print("empty now ")

