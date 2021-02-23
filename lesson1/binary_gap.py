
def solution(N):
    squared = 1
    while N > squared:
        squared *= 2
    binary = ""
    if N < squared:
        squared = int(squared / 2)
    while N >= 1:
        if N >= squared:
            N = N % squared
            binary += "1"
        else:
            binary += "0"
        if squared == 1:
            continue
        squared = int(squared / 2)

    arr = []
    cnt = 0
    for b in binary:
        if b == "1":
            arr.append(cnt)
        cnt = cnt + 1
    max = 0
    for i in range(len(arr)-1):
        if arr[i+1] - arr[i] > max:
            max = arr[i+1] - arr[i]
    if max == 0:
        return 0
    else:
        return max-1


if __name__ == '__main__':
    print(solution(1041))
