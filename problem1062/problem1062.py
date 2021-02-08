from itertools import combinations

n, k = map(int, input().split())
word_list = [input() for _ in range(n)]
alphabet_bit_list = [0 for _ in range(26)]
need = ['b', 'd', 'e', 'f', 'g', 'h', 'j', 'k', 'l', 'm', 'o', 'p', 'q', 'r', 's', 'u', 'v', 'w', 'x', 'y', 'z']
base = ['a', 'c', 't', 'i', 'n']


for alphabet in base:
    alphabet_bit_list[97 - ord(alphabet)] = 1
max_count = 0

if k < 5:
    print(0)
elif k == 5:
    for word in word_list:
        flag = True

        for alphabet in word:
            if alphabet_bit_list[97 - ord(alphabet)] == 0:
                flag = False
                break
        if flag:
            max_count += 1
else:
    for combi in list(combinations(need, k - 5)):
        count = 0
        temp_list = alphabet_bit_list[:]

        for alphabet in combi:
            temp_list[97 - ord(alphabet)] = 1
        for word in word_list:
            flag = True

            for alphabet in word:
                if temp_list[97 - ord(alphabet)] == 0:
                    flag = False
                    break
            if flag:
                count += 1
        max_count = max(max_count, count)

print(max_count)