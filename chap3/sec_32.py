count = int(input())
num_list = [int(i) for i in input().split()]
maped_list = map(str, num_list)
print(' '.join(maped_list))

for i in range(1,count):
    num = num_list[i]
    j = i - 1
    while j >= 0 and num_list[j] > num:
        num_list[j + 1] = num_list[j]
        j = j - 1
    num_list[j + 1] = num
    maped_list = map(str, num_list)
    print(' '.join(maped_list))
# maped_list = map(str, num_list)
# moji = ' '.join(maped_list)
# print(moji)
