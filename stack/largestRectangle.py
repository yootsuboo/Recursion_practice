# def largestRectangle(h):
#     results = [0] * len(h)

#     for i in range(len(h)):
#         j = i - 1
#         total = 1
#         curr = h[i]
#         while j >= 0 and curr <= h[j]:
#             total += 1
#             j -= 1
#         j = i + 1
#         while j < len(h) and curr <= h[j]:
#             total += 1
#             j += 1
#         results[i] = total * curr

#     return max(results)


def stackCounter(arr):
    stack = []
    results = [0] * len(arr)
    i = 0
    for x in  arr:
        total = 1
        while len(stack) != 0 and arr[stack[-1]] >= x:
            j = stack.pop()
            total += results [j]

        stack.append(i)
        results[i] = total
        i += 1

    return results

def largestRectangle(h):
    left = stackCounter(h)
    right = stackCounter(h[::-1])[::-1]

    total = [(left[i] + right[i]-1) * h[i] for i in range(len(h))]
    return max(total)

