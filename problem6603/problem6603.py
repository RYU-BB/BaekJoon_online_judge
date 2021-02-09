from itertools import combinations


while True:
    input_list = list(map(int, input().split()))
    if input_list[0] == 0:
        break
    else:
        num_list = input_list[1:]

    for num_list in list(combinations(num_list, 6)):
        for num in num_list:
            print(num, end=" ")
        print()
    print()
