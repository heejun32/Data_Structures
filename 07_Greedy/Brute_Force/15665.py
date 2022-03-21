import sys
input = sys.stdin.readline

N, M = map(int, input().split())
L = sorted(map(int, input().split()))
S = [0] * N


def backtracking(K):
    if K == M:
        for m in range(M):
            print(S[m], end=' ')
        print()
        return None
    check = 0
    for n in range(N):
        if check != L[n]:
            S[K] = L[n]
            check = L[n]
            backtracking(K + 1)


backtracking(0)
