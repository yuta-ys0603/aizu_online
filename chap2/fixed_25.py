count = int(input())
num_list = [int(input()) for i in range(count)]
max_price = -999999999999999

min_num = num_list[0]

for i in range(1,len(num_list)):
    differ = num_list[i] - min_num

    if differ > max_price:
        max_price = differ

    if min_num > num_list[i]:
        min_num = num_list[i]

print (max_price)
