n = int(input())
S = input().split()
q = int(input())
T = input().split()
count = 0

for i in T:
    if i in S:
        count += 1

print(count)
