def stockSpan(stocks):
    stack = []
    results = []

    for i in range(len(stocks)):
        current = stocks[i]
        counter = 1

        while len(stack) > 0 and stocks[stack[-1]] < current:
            counter += results[stack.pop()]

        results.append(counter)
        stack.append(i)

    return results

print(stockSpan([30,50,60,20,30,64,80]))
