# 要素の組合せを調べる
from itertools import combinations as com

n = int(input())
A = [int(i) for i in input().split()]
q = int(input())
m = [int(i) for i in input().split()]

# in参照の速度
# set < dict < list
sum_lt = set()

for i in range(1,n+1):
    for j in com(A,i):
        sum_lt.add(sum(j))

# print (sum_lt)

for i in m:
    if i in sum_lt:
        print('yes')
    else:
        print('no')
