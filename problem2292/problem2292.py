n = int(input())
count = 0
i = 1
if(n==1):
    count=1
while(i<n):
    i += 6*count
    count += 1
print(count)