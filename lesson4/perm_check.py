def solution(A):
    A.sort()
    for i in range(len(A)):
        if not A[i] == i + 1:
            return 0
    return 1


if __name__ == '__main__':
    # A = [4, 1, 3, 2]
    A = [4, 1, 3]
    print(solution(A))
