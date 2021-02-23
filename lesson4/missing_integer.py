

def solution(A):
    A.sort()
    result = 1
    if A[0] > 1:
        return result
    for i in range(len(A)-1):
        if A[i] < 0:
            continue
        if A[i] == A[i+1] or A[i] == A[i+1] - 1:
            result = A[i + 1]
        else:
            result = A[i] + 1
            break
    if result == A[len(A)-1]:
        result = result + 1
    return result


if __name__ == '__main__':
    # A = [1, 3, 6, 4, 1, 2]
    # A = [1, 2, 3]
    # A = [1]
    # A = [(-1), (-3), 0, 2, 3]
    A = [4, 5, 6, 2]

    print(solution(A))
