
def calc_min(price,num_list):

    for i  in range(len(num_list) - 1):
        # for j in range(i+1,len(num_list)):
        #     if price < (num_list[j] - num_list[i]):
        #         price = num_list[j] - num_list[i]

        differ = max(num_list[i+1:]) - num_list[i]
        if price < differ:
            price = differ

    return price

# i番目から先の最大値とi番目の差がmaxのもの？
# runtime 25 -> 35
if __name__ == '__main__':

    # max_price = -999999999999999
    # num_list = []
    # count = int(input())
    # for i in range(count):
    #     num = int(input())
    #     num_list.append(num)

    count = int(input())
    num_list = [int(input()) for i in range(count)]
    max_price = -999999999999999

    max_price = calc_min(max_price,num_list)

    print (max_price)
