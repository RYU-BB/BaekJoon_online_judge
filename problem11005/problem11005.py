input_num, base_n = map(int, input().split())
result = ""

while input_num > 0:
    remainder = input_num % base_n
    if remainder >= 10:
        result += chr(65 + (remainder - 10))
    else:
        result += str(remainder)

    input_num = input_num // base_n

print(result[::-1])
