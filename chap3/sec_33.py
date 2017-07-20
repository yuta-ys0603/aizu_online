count = int(input())
num_list = [int(i) for i in input().split()]
flag = 1
loop_count = 0

while flag:
    flag = 0
# for i in range(n,0,-1)で逆順にループ可能
    for i in reversed(range(1,len(num_list))):
        if num_list[i] < num_list[i - 1]:
            v = num_list[i]
            num_list[i] = num_list[i - 1]
            num_list[i - 1] = v

            flag = 1
            loop_count += 1

maped_list = map(str, num_list)
print(' '.join(maped_list))
print(count)
