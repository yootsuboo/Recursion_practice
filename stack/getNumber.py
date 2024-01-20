def getNumber(code):
    if len(code) > 8:
        return "0"

    stack = []
    res = ""

    for i in range(0, len(code)+1):
        stack.append(i+1)
        if i == len(code) or code[i] == "I":
            while len(stack) > 0:
                res += str(stack.pop())

    return res
    

