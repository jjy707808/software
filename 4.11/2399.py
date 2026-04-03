a = int(input())
b = list(map(int, input().split()))

b.sort()

prefix = 0
answer = 0

for i in range(a):
    answer += b[i] * i - prefix
    prefix += b[i]

print(answer * 2)