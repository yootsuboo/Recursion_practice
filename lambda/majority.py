import math

def majority(f, arr):
    middle = math.floor(len(arr) / 2 )
    return [f(i) for i in arr].count(True) > middle

def isOdd(n: int) -> bool:
    return n % 2 != 0

def isEven(n: int) -> bool:
    return n % 2 == 0


print(majority(isOdd, [1,2,3,4,5])) #--> true
print(majority(isOdd, [2,4,6,7,8])) #--> false
print(majority(isEven, [3,6,8,12,15])) #--> true
print(majority(isEven, [4,5,7,11,14])) #--> false

"""
過半数
easy
整数の配列と特定の処理を行うコールバック関数 f を受け取り、配列内の要素に対して f を適用した結果、その過半数が true であるかどうかを判定する majority 関数を作成してください。各コールバック関数は、以下の通りです。

bool isOdd(int n)
整数 n が奇数であれば true、偶数であれば false を返します。

bool isEven(int n)
整数 n が偶数であれば true、奇数であれば false を返します。

majority 関数

入力：
（Function）関数の参照
（array）整数の配列
出力：
（bool 型）true が過半数であれば true、そうでなければ false を返します。
テストケース

majority(isOdd, [1,2,3,4,5]) --> true

majority(isOdd, [2,4,6,7,8]) --> false

majority(isEven, [3,6,8,12,15]) --> true

majority(isEven, [4,5,7,11,14]) --> false
"""
