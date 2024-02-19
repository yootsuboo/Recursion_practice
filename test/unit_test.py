"""
自動テストI
easy
Henin は、自然数 n の階乗を計算する factorial 関数を再帰的に作成しました。彼女はこの関数の動作を自動的にテストしたいと考えています。この目的のため、彼女は汎用的な自動テスト関数 unitTests を作成することにしました。unitTests 関数は、テストの入力値を表す配列 inputs と、それらの入力に対応する期待される出力値を表す配列 outputs を引数として受け取ります。そして、unitTests 関数内で factorial 関数の動作が期待通りであることを確認するために、factorialCheck 関数を呼び出します。

テストの結果を報告するために、unitTestCheck という関数を使用します。この関数は、渡された条件（述語）が真か偽かを判定し、それに基づいてテストが成功したか失敗したかをコンソールに表示します。factorialCheck 関数は、factorial 関数の出力が期待される結果と一致するかどうかをチェックするために使われます。この関数は、factorial 関数によって計算された値と、期待される正しい結果を比較し、両者が等しい場合に真を、そうでない場合に偽を返します。

例えば、unitTests 関数は以下のような配列を引数として持ちます。この関数は、各入力値に対して factorialCheck を呼び出し、その結果を unitTestCheck 関数に渡して、テストが成功したかどうかを報告します。
    第一引数：入力の配列 [2,3,5]
    第二引数：入力にマッピングされる正しい出力 [2,6,120]

テストケース
unitTests([1,2,3,4,5,6,7,8],[1,1,6,24,130,720,5040,42000])
"""

def factorial(n):
    if n == 0: return 1
    return n * factorial(n-1)

def factorialCheck(number, result):
    # factorial関数の整合性をチェックしてください
    return factorial(number) == result

def unitTestCheck(predicate):
    if predicate: 
        print("The test passed!!")
    else:
        print("ERROR! The test failed!!")

def unitTests(inputs, outputs):
    # ここから書いてください
    for inputNum, outputNum in zip(inputs, outputs):
        unitTestCheck(factorialCheck(inputNum, outputNum))


unitTests([1,2,3,4,5,6,7,8],[1,1,6,24,130,720,5040,42000])
