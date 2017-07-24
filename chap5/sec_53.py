n = int(input())
S = [int(i) for i in input().split()]
q = int(input())
T = [int(i) for i in input().split()]
count = 0
left = 0
right = len(S)

for i in T:
    left = 0
    right = len(S)

    while right > left:
        mid = int((left + right)/2)

        if i == S[mid]:
            count += 1
            break
        elif i >= S[mid]:
            left = mid + 1
        else:
            right = mid

print(count)
# cp_list = S[:]
# for i in T:
#     mid = int(len(S) / 2)
#     cp_list = S[:]
#
#     while len(cp_list) > 0:
#         if i == cp_list[mid]:
#             count += 1
#             break
#         elif i >= cp_list[mid]:
#             cp_list = cp_list[mid+1:]
#         else:
#             cp_list = cp_list[:mid]
#
#         mid = int(len(cp_list) / 2)
