# LIFO order
# Push & Pop operations  --> append and pop

stack = []
stack.append(10)
stack.append(20)
stack.append(30)
print(stack)

print(stack.pop())
print(stack.pop())
print(stack)

len(stack) == 0

print(not stack)

print(stack[-1])
