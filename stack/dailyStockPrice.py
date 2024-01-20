def dailyStockPrice(stocks):
    stack = []
    res = [0] * len(stocks)
    # インデックスを後ろから追跡
    for i in range(len(stocks) -1, -1, -1):
        while len(stack) > 0 and stocks[stack[-1]] <= stocks[i]: stack.pop()
        if len(stack) > 0: res[i] = stack[-1] - i
        stack.append(i)
        print(stack)

    return res

'''
input : [480,733,225,39,939,756,51,887,188,412,180,714,303,782,34,984]
stack:
[15]
[15, 14]         # 前の値が小さかったらインデックスを追加
[15, 13]         # 大きかったら小さくなるまで取り出して現在のインデックスを追加
[15, 13, 12]     # インデックスの差分が株価が高くなった日となる
[15, 13, 11]     # res[i] を0からインデックスの差分で上書き
[15, 13, 11, 10]
[15, 13, 11, 9]
[15, 13, 11, 9, 8]
[15, 7]
[15, 7, 6]
[15, 7, 5]
[15, 4]
[15, 4, 3]
[15, 4, 2]
[15, 4, 1]
[15, 4, 1, 0]
'''
