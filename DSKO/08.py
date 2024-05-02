s = input()

stack = []

total = 0
for temp in s:
    if temp == '(':
        total += 1
    elif temp == ')':
        total -= 1
print(total == 0)