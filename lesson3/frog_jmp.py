
def runtime_error_solution(X, Y, D):
    if X == Y:
        return 0
    if (Y-X) % D:
        return (Y-X)//D + 1
    else:
        return (Y-X)/D


def solution(X, Y, D):
    if X == Y:
        return 0
    if (Y-X) % D:
        return (Y-X)//D + 1
    else:
        return (Y-X)//D


if __name__ == '__main__':
    X = 1
    Y = 5
    D = 2
    print(solution(X, Y, D))
