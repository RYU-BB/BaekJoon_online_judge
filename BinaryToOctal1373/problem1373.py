binary = input()

while len(binary) % 3 != 0:
    binary = '0' + binary

for i in range(len(binary) // 3):
    octal = 0
    for j in range(3):
        octal += int(binary[3 * i + j]) * (2 ** (2 - j))
    print(octal, end='')
