def solution(input):
    print(input)
    cSum = input[0]
    cSumMax = input[0]
    print('i =', 0, '\tvalue =', input[0], '\tcSum =', cSum, '\tcSumMax =', cSumMax)
    for i in range(1, len(input)):
        value = input[i]
        cSum = max(cSum + value, value)
        cSumMax = max(cSumMax, cSum)
        print('i =', i, '\tvalue =', input[i], '\tcSum =', cSum, '\tcSumMax =', cSumMax)


a = [-1, 3, -1, 5]
solution(a)

a = [-5, -3, -1]
solution(a)

a = [2, 4, -2, -3, 8]
solution(a)
