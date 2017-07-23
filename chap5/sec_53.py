n = int(input())
S = [int(i) for i in input().split()]
q = int(input())
T = [int(i) for i in input().split()]
count = 0

for i in T:
    mid = int(len(S) / 2)
    copy_list = S[:]

    while len(copy_list) > 0:
        if i == copy_list[mid]:
            count += 1
            break
        elif i >= copy_list[mid]:
            copy_list = copy_list[mid+1:]
        else:
            copy_list = copy_list[:mid]

        mid = int(len(copy_list) / 2)

print(count)
