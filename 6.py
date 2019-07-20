def hasil(N):
    string = ''
    num_list = []
    
    for i in range(1, N+1):
        string += str(i)
    
    for c in string:
        num_list.append(int(c))
    
    return num_list

def mrBrulee(func, N, arr):
    num_list = hasil(N)
    num_picked = []
    
    for i in arr:
        num_picked.append(num_list[i-1])
    
    if func == "SUM":
        result = 0
        for i in num_picked:
            result += i
    elif func == "MUL":
        result = 1
        for i in num_picked:
            result *= i
    elif func == "SUB":
        result = num_picked[0] * 2
        for i in num_picked:
            result -= i
    elif func == "DIV":
        result = num_picked[0] * num_picked[0]
        for i in num_picked:
            result /= i
    
    return result

print(mrBrulee('SUM',20,[11,13,15]))
print(mrBrulee('MUL',20,[12,15,17]))
print(mrBrulee('SUB',20,[11,13,15]))
print(mrBrulee('DIV',20,[12,15,17]))