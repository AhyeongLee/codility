def solution(A):
    if len(A) == 2:
        return abs(A[0]-A[1])
    memo = []
    sum = 0
    for a in A:
        sum = sum + a
        memo.append(sum)
    min = 100000000
    for p in range(1, len(A)):
        left = memo[p-1]
        right = memo[len(memo)-1] - memo[p-1]
        if min > abs(left - right):
            min = abs(left - right)
    return min


if __name__ == '__main__':
    A = [1, 1, 3]
    # A = []
    # for i in range(100000):
    #     A.append(i)
    # A[0] = 4999950000
    # print(sum(A))

# 100,000
    print(solution(A))
