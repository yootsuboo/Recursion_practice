def customArray(f, arr):
    for i in range(len(arr)):
        print(f(arr[i]))
    

def cube(n: int) -> int:
    return n ** 3

def splitAndAdd(n: int) -> int:
    return sum(int(digit) for digit in str(n))


customArray(cube, [3, 11, 24, 31])
# --> 27
# --> 1331
# --> 13824
# --> 29791

customArray(splitAndAdd, [3, 11, 24, 31])
# --> 3
# --> 2
# --> 6
# --> 4

"""
カスタム配列
easy
自然数の配列と、配列の各要素に特定の処理を実行するコールバック関数 f を引数として受け取る customArray 関数を作成してください。この関数は、引数で与えられたコールバック関数 f を使用して配列の各要素に処理を施し、その結果を新しい配列の要素として順に出力します。各コールバック関数は、以下の通りです。

int cube(int n)
整数 n を受け取って、3 乗にして返す関数。

int splitAndAdd(int n)
整数 n を受け取って、全ての桁数を合計して返す関数。

customArray 関数

入力：
（Function）関数の参照
（array）自然数の配列
出力：
（void）配列の各要素にコールバック関数 f を適用した結果を順にコンソールに出力
"""
