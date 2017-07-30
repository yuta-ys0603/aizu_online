def pertition(A, p, r):
    x = A[r]
    i = p - 1
    for j in range(p,r):
        if A[j] <= x:
            i += 1
            A[i], A[j] = A[j], A[i]
    A[i + 1], A[r] = A[r], A[i + 1]
    return i + 1

n = int(input())
A = list(map(int,input().split()))
idx = pertition(A, 0, n-1)

for i in range(n):
    if i == n - 1:
        print(str(A[i]))
    elif i == idx:
        print('[' + str(A[idx]) + '] ', end = '')
    else:
        print(str(A[i]) + ' ', end = '')
