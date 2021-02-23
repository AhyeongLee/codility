from collections import deque


def solution(A, K):
    deA = deque(A)
    for i in range(K):
        deA.rotate(1)
    return list(deA)


if __name__ == '__main__':
    testcase = [
        ([3, 8, 9, 7, 6], 3),
        ([0, 0, 0], 1)
    ]
    for t in testcase:
        print(solution(t[0], t[1]))
