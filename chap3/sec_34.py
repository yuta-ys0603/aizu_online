count = int(input())
num_list = [int(i) for i in input().split()]
loop_count = 0

for i in range(0,count):
    min_j = i

    for j in range(i,count):
        if num_list[j] < num_list[min_j]:
            min_j = j

    if num_list[min_j] < num_list[i]:
        v = num_list[min_j]
        num_list[min_j] = num_list[i]
        num_list[i] = v
        loop_count += 1

maped_list = map(str, num_list)
print(' '.join(maped_list))
print(loop_count)
