
def calc_min(price,num_list):

    for i  in range(len(num_list) - 1):

        differ = max(num_list[i+1:]) - num_list[i]
        if price < differ:
            price = differ

    return price

if __name__ == '__main__':

    count = int(input())
    num_list = [int(input()) for i in range(count)]
    max_price = -999999999999999

    max_price = calc_min(max_price,num_list)

    print (max_price)
