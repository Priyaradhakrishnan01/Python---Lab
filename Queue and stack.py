stack = []

print("--- Stack ---")
stack.append(10)
stack.append(20)
stack.append(30)
print("Stack:", stack)

print("Peek:", stack[-1])
stack.pop()
print("After Pop:", stack)

queue = []

print("\n--- Queue ---")
queue.append(10)
queue.append(20)
queue.append(30)
print("Queue:", queue)

queue.pop(0)
print("After Dequeue:", queue)

