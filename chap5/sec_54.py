n = int(input())
dic = {}

for i in range(n):
    com,num = input().split()

    if com == 'insert':
        dic[num] = num
    elif com == 'find':
        if num in dic:
            print('yes')
        else:
            print('no')
# dic = []
#
# for i in range(n):
#     com, num = input().split()
#     if com == 'insert':
#         dic.append(num)
#     elif com == 'find':
#         if num in dic:
#             print('yes')
#         else:
#             print('no')
