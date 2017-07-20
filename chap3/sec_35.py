def BubbleSort(count,num_list):
    flag = 1
    while flag:
        flag = 0

        for i in reversed(range(1,len(num_list))):
            if num_list[i][1] < num_list[i - 1][1]:
                v = num_list[i]
                num_list[i] = num_list[i - 1]
                num_list[i - 1] = v
                flag = 1

    return num_list

def SelectionSort(count,num_list):
    for i in range(0,count):
        min_j = i

        for j in range(i,count):
            if num_list[j][1] < num_list[min_j][1]:
                min_j = j

        if num_list[min_j][1] < num_list[i][1]:
            v = num_list[min_j]
            num_list[min_j] = num_list[i]
            num_list[i] = v

    return num_list

def isStable(num_list,sorted_list):
    N = len(num_list)
    flag = 1
    for i in range(0,N):
        for j in range(i+1,N):
            for a in range(0,N):
                for b in range(a+1,N):
                    if num_list[i][1] == num_list[j][1] and num_list[i] == sorted_list[b] and num_list[j] == sorted_list[a]:
                        print("Not stable")
                        flag = 0
                        return 
    if flag:
        print("Stable")

count = int(input())
num_list = [i for i in input().split()]

bubble_list = num_list.copy()
selection_list = num_list.copy()

bubble_list = BubbleSort(count,bubble_list)
selection_list = SelectionSort(count,selection_list)

print(' '.join(map(str,bubble_list)))
isStable(num_list,bubble_list)
print(' '.join(map(str, selection_list)))
isStable(num_list,selection_list)


#list[0][1] リスト1番目の要素のインデックス1の文字列を取得
