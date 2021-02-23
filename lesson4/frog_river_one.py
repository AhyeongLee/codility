def solution(X, A):
    memo = []
    for i in range(X):
        memo.append(1000000)
    for i in range(len(A)):
        if memo[A[i]-1] > i:
            memo[A[i]-1] = i
    memo.sort()
    if memo[len(memo)-1] == 1000000:
        return -1
    return memo[len(memo)-1]


if __name__ == '__main__':
    # A = [1, 3, 1, 4, 2, 3, 5, 4]
    # A = [1, 2, 3, 4, 5, 6, 7]
    A = []
    for i in range(100000):
        A.append(i+1)
    X = 100000
    print(solution(X, A))
