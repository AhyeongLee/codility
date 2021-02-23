def solution(A, B, K):
    if K == 1:
        return B - A + 1
    start = 1
    if A % K == 0:
        if A >= K:
            start = A//K
        elif A == 0:
            start = 0
    elif A > K:
        tmp = K
        cnt = 0
        while tmp < A:
            cnt = cnt + 1
            tmp = K * cnt
        start = cnt

    end = B//K
    print(start*K, end*K)

    return end - start + 1


if __name__ == '__main__':
    A = 0
    B = 13
    K = 2
    print(solution(A, B, K))

# A and B are integers within the range [0..2,000,000,000];
# K is an integer within the range [1..2,000,000,000];
# A ≤ B.
