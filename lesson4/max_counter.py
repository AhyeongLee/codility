def timeout_solution(N, A):
    result = [0] * N
    max = 0
    for i in range(len(A)):
        if A[i] < N + 1:
            result[A[i] - 1] = result[A[i] - 1] + 1
            if max < result[A[i] - 1]:
                max = result[A[i] - 1]
        elif A[i] == N + 1:
            for j in range(len(result)):
                result[j] = max
    return result


def solution(N, A):
    result = [0] * N
    potential_max = 0
    max = 0
    for i in range(len(A)):
        if A[i] < N + 1:
            index = A[i] - 1
            if result[index] < max:
                result[index] = max
            result[index] = result[index] + 1
            if potential_max < result[index]:
                potential_max = result[index]
        else:
            max = potential_max

    for i in range(len(result)):
        if result[i] < max:
            result[i] = max
    return result


if __name__ == '__main__':
    A = [3, 4, 4, 6, 1, 4, 4]
    # A = []
    # for i in range(100000):
    #     A.append(100001)
    N = 5
    print(solution(N, A))
