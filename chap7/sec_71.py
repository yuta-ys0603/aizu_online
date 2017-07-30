import sys

def merge(A, left, mid, right):
    # n1 = mid - left
    # n2 = right - mid
    global cnt
    i = 0
    j = 0

    L = A[left:mid]
    L.append(1000000000)
    R = A[mid:right]
    R.append(1000000000)

    # for i in range(n1):
    #     L[i] = A[left + i]
    # for i in range(n2):
    #     R[i] = A[mid + i]

    for k in range(left, right):
        if L[i] <= R[j]:
            A[k] = L[i]
            i += 1
        else:
            A[k] = R[j]
            j = j + 1
    cnt += i + j

def mergeSort(A, left, right):
    if left + 1 < right:
        mid = int((left + right) / 2)
        mergeSort(A, left, mid)
        mergeSort(A, mid, right)
        merge(A, left, mid, right)

n = int(input())
# S = [int(i) for i in input().split()]
S = list(map(int,input().split()))
cnt = 0
mergeSort(S, 0, n)
print(' '.join(map(str,S)))
print(cnt)
