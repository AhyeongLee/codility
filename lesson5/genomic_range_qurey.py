
def timeout_solution(S, P, Q):
    s_num = []
    for i in range(len(S)):
        n = 0
        if S[i] == "A":
            n = 1
        elif S[i] == "C":
            n = 2
        elif S[i] == "G":
            n = 3
        elif S[i] == "T":
            n = 4
        s_num.append(n)
    result = []
    for i in range(len(P)):
        min = 5
        for j in range(P[i], Q[i]+1):
            if min > s_num[j]:
                min = s_num[j]
        result.append(min)
    return result

# https://nachwon.github.io/GenomicRangeQuery/


def solution(S, P, Q):
    prefix = [[0, 0, 0, 0]]
    for i in range(len(S)):
        n = 0
        if S[i] == "A":
            n = 0
        elif S[i] == "C":
            n = 1
        elif S[i] == "G":
            n = 2
        elif S[i] == "T":
            n = 3
        tmp = prefix[i][:]
        for j in range(4):
            if j == n:
                tmp[n] = tmp[n]+1
                break
        prefix.append(tmp)
    result = []
    for i in range(len(P)):
        for j in range(4):
            if 0 < prefix[Q[i]+1][j] - prefix[P[i]][j]:
                result.append(j+1)
                break

    return result


if __name__ == '__main__':
    # S = "C"*100000
    # P = [0]*50000
    # Q = [99999]*50000
    S = "CAGCCTA"
    P = [2, 5, 0]
    Q = [4, 5, 6]
    print(solution(S, P, Q))

# N is an integer within the range [1..100,000];
# M is an integer within the range [1..50,000];
# each element of arrays P, Q is an integer within the range [0..N − 1];
# P[K] ≤ Q[K], where 0 ≤ K < M;
# string S consists only of upper-case English letters A, C, G, T.
