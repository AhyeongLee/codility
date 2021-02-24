def solution(K, A):
    count = 0
    sum = 0
    for i in range(len(A)):
        if A[i] >= K:
            count += 1
            sum = 0
            continue
        sum += A[i]
        if sum >= K:
            count += 1
            sum = 0
            continue
    return count


if __name__ == '__main__':
    K = 6
    A = [1, 2, 3, 4, 1, 1, 2, 3, 3, 2]
    # A = [1, 2, 3, 4, 1, 1, 3]
    # A = [1, 2]
    # A = [1]
    print(solution(K, A))

# N is an integer within the range [1..100,000];
# K is an integer within the range [1..1,000,000,000];
# each element of array A is an integer within the range [1..1,000,000,000].
