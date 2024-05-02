num = int(input())

stack = []

while num != 0:
    stack.append(str(num % 2))
    num = num // 2

binary_number = ''.join(stack[::-1])  # Die Elemente umdrehen und dann zu einem String zusammenfügen

print(binary_number)