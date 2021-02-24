min = 100000


def calc(A, i, sum):
    global min
    if i == len(A)-1:
        if min > abs(sum + A[i]):
            min = abs(sum + A[i])
        if min > abs(sum + A[i]*(-1)):
            min = abs(sum + A[i]*(-1))
        return
    calc(A, i+1, sum + A[i])
    calc(A, i+1, sum + A[i]*(-1))


def timeout_solution(A):
    if len(A) == 0:
        return 0
    elif len(A) == 1:
        return abs(A[0])
    calc(A, 0, 0)
    return min


if __name__ == '__main__':
    A = [1, 5, 2, 3]
    print(solution(A))


# N is an integer within the range [0..20,000];
# each element of array A is an integer within the range [−100..100].
