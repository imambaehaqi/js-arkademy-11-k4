def evenSum(N):
    if (N < 2):
        return 0

    prevNumber = 0
    currNumber = 2
    result = prevNumber + currNumber

    while (currNumber < N):
        nextNumber = 4 * currNumber + prevNumber
        
        if (nextNumber > N):
            break

        prevNumber = currNumber
        currNumber = nextNumber
        result += currNumber

    return result

def oddSum(N):
    prevNumber = 1
    currNumber = 1
    result = 0
    
    while (currNumber < N):
        if (currNumber % 2 != 0):
            result += currNumber

        currNumber += prevNumber
        prevNumber = currNumber - prevNumber

    return result

print(evenSum(1000))
print(oddSum(100))
print(oddSum(1000))