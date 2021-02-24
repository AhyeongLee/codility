
def solution(A, B):
    if len(A) == 0:
        return 0
    elif len(A) == 1:
        return 1
    result = []
    result.append(0)
    for i in range(1, len(A)):
        if B[result[-1]] >= A[i]:
            # 겹칠때
            if B[result[-1]] > B[i]:
                result.pop()
                result.append(i)
        else:
            result.append(i)

    return len(result)


if __name__ == '__main__':
    A = [1, 3, 7, 9, 9]
    B = [5, 6, 8, 9, 10]
    print(solution(A, B))

# N is an integer within the range [0..30,000];
# each element of arrays A, B is an integer within the range [0..1,000,000,000];
# A[I] ≤ B[I], for each I (0 ≤ I < N);
# B[K] ≤ B[K + 1], for each K (0 ≤ K < N − 1).
