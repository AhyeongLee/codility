def solution(A):
    A.sort()
    for i in range(len(A)):
        if not (i + 1) == A[i]:
            return (i+1)
    return len(A)+1


if __name__ == '__main__':
    A = [1, 2, 3, 4]

    print(solution(A))
