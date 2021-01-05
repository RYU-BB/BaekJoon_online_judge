base_a, base_b = map(int, input().split())
m = int(input())
nums = [int(x) for x in input().split()]

num = 0
result = ""

for i in range(1, m + 1):
    num += nums[-i] * (base_a ** (i - 1))

while num:
    result = str(num % base_b) + " " + result
    num = num // base_b

print(result)