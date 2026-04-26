def solution(polynomial):
    x_sum = 0
    num_sum = 0
    
    terms = polynomial.split(" + ")
    
    for term in terms:
        if "x" in term:
            if term == 'x':
                x_sum += 1
            else:
                x_sum += int(term.replace("x"," "))
        else:
            num_sum += int(term)
        result = []

    if x_sum > 0:
        if x_sum == 1:
            result.append("x")
        else:
            result.append(str(x_sum) + "x")

    if num_sum > 0:
        result.append(str(num_sum))

    return " + ".join(result)