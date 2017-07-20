def insertionSort(A,n,g):
    cnt = 0

    for i in range(g,n):
        v = A[i]
        j = i - g

        while j >= 0 and A[j] > v:
            A[j+g] = A[j]
            j = j - g
            cnt += 1
        A[j + g] = v

    return cnt

def shellSort(A,n):
    total_cnt = 0
    G = [1]

    for i in range(1,n):
        G.append(3 * G[i-1] + 1)

    reversed(G)
    m = len(G)

    for i in range(m):
        total_cnt =  total_cnt + insertionSort(A,n,G[i])

    return m,G,total_cnt

n = int(input())
num_list = [int(input()) for i in range(n)]
m,G,total_cnt = shellSort(num_list,n)

print(m)
print(' '.join(map(str,G)))
print(total_cnt)
print('\n'.join(map(str,num_list)))
