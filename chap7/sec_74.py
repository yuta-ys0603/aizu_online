def CountingSort(A, B, k):
    n = len(A)

    C = [0 for i in range(k+1)]

    for j in range(n):
        C[A[j]] += 1

    for i in range(1, k+1):
        C[i] = C[i] + C[i - 1]

    for j in range(n-1,-1,-1):
        B[C[A[j]]-1] = A[j]
        C[A[j]] -= 1
    return B

n = int(input())
A = list(map(int, input().split()))
B = [0 for i in range(n)]
B = CountingSort(A, B, max(A))
print(' '.join(map(str,B)))
