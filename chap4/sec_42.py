num_list = [i for i in input().split()]
stack = []

for i in num_list:
    if i == '+':
        n1 = int(stack.pop())
        n2 = int(stack.pop())
        stack.append(n2 + n1)
    elif i == '-':
        n1 = int(stack.pop())
        n2 = int(stack.pop())
        stack.append(n2 - n1)
    elif i == '*':
        n1 = int(stack.pop())
        n2 = int(stack.pop())
        stack.append(n2 * n1)
    else:
        stack.append(i)

print (stack[0])
