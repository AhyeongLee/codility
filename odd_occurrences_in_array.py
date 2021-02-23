# Timeout
def timeout_solution(A):
    result = []
    for i in range(len(A)):
        if len(result) == 0:
            result.append(A[i])
            continue
        has = False
        for r in result:
            if r == A[i]:
                result.remove(r)
                has = True
                break
        if not has:
            result.append(A[i])

    return result[0]


def solution(A):
    if len(A) == 1:
        return A[0]
    A.sort()
    for i in range(0, len(A), 2):
        if i == len(A)-1 or not A[i] == A[i+1]:
            return A[i]


if __name__ == '__main__':
    A = [1, 1, 1, 1, 5]
    print(solution(A))
