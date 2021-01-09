"""problem 2302
vip 각 좌석번호의 왼쪽 좌석의 개수가 가질 수 있는 모든 경우의 수와
마지막 vip 좌석의 오른쪽 좌석의 개수가 가질 수 있는 모든 경우의 수를 곱해 모든 경우의 수를 구한다.

직전의 vip좌석의 번호를 저장해 새로 입력받은 vip좌석번호 - 이전 vip좌석번호로 vip좌석 사이에 존재하는 좌석의 개수를 구한다.
"""
n = int(input())
num_case = [1] * (n + 1)
num_case[1] = 1
result = 1
vip = 0
pre_vip = 0

for i in range(2, n + 1):
    num_case[i] = num_case[i - 1] + num_case[i - 2]

m = int(input())

for _ in range(m):
    vip = int(input())
    result *= num_case[vip - pre_vip - 1]
    pre_vip = vip

result *= num_case[n - vip]

print(result)