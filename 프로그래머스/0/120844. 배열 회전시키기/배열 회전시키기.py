def solution(numbers, direction):
    for i in range(0,len(numbers)+1):
        if direction == "right":
            return [numbers[-1]] + numbers[:-1]
        else:
            return numbers[1:] + [numbers[0]]