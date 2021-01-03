import sys

stack = list()

num = int(input())
max = 0
result = ""

for _ in range(num):
    input_num = int(input())

    if input_num > max:
        while input_num > max:
            result += "+\n"
            max += 1
            stack.append(max)
        stack.pop()
        result += "-\n"
    else:
        top = stack.pop()
        result += "-\n"
        if top < input_num:
            print("NO")
            sys.exit()
        elif stack:
            while stack[-1] > input_num:
                stack.pop()
                result += "-\n"

print(result)
