# deque(デック)は両端での追加や削除が高速で行えるリストのようなコンテナ
# double ended queue : 両端キュー
# d = deque{("name", "age"])
# d.append("gender") # 右端への追加
# d.appendleft("id") # 左端への追加
# last = d.pop() # 右端からの削除
# first = d.popleft() # 左端からの削除
from collections import deque

def expressionParser(expression):
    nums = deque([])
    ops = deque([])

    i = 0
    while i < len(expression):
        # isdight() : 数字か判断
        if not expression[i].isdigit():
            # 数字ではなかったら演算子なので演算子の優先順位で処理を振り分けていく
            currOP = expression[i]

            while len(ops) > 0 and getPriority(currOP) <= getPriority(ops[-1]):
                process(nums, ops.pop())
            ops.append(currOP)

        else:
            number = ""
            while i < len(expression) and expression[i].isdigit():
                number += expression[i]
                i += 1

            i -= 1
            nums.append(int(number))

        i += 1

    while len(ops) > 0:
        process(nums, ops.pop())

    return nums[0]

def process(stack, op):
    right = int(stack.pop())
    left = int(stack.pop())

    value = 0

    if op == "+": value = left + right
    if op == "-": value = left - right
    if op == "*": value = left * right
    if op == "/" and right == 0: value = left
    elif op == "/": value = left // right

    stack.append(value)

def getPriority(op):
    if op == "+" or op == "-": return 1
    elif op == "*" or op == "/": return 2

    
