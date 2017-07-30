def pertition(A, p, r):
    x = A[r][1]
    i = p - 1
    for j in range(p,r):
        if A[j][1] <= x:
            i += 1
            A[i], A[j] = A[j], A[i]
    A[i + 1], A[r] = A[r], A[i + 1]
    return i + 1

def quickSort(A, p, r):
    if p < r:
        q = pertition(A, p, r)
        quickSort(A, p, q-1)
        quickSort(A, q+1, r)

def isStable(n, A, B):
    for i in range(n):
        if A[i][0] != B[i][0]:
            return False
    return True

n = int(input())
A = []

for i in range(n):
    A.append(input().split())
    A[i][1] = int(A[i][1])

B = A[:]
# 多次元ソート
B.sort(key=lambda x:x[1])
quickSort(A, 0, n-1)
print('Stable' if isStable(n, A, B) else 'Not stable')

for i in A:
    print('{} {}'.format(i[0], i[1]))
