def solution(intStrs, k, s, l):
    answer = []
    
    for i in range(len(intStrs)):
        part = intStrs[i][s:s+l]
        new_val = int(part)
        
        if new_val > k:
            answer.append(new_val)
    return answer