def solution(arr):
    stk = []

    for num in arr:
        if not stk:
            stk.append(num) 
        elif stk[-1] == num:
            stk.pop()
        else:
            stk.append(num)

    return stk if stk else [-1]