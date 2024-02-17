"""
デコレータ
medium
Ken のタスクは、配列の合計値を計算する既存の関数 sumOfArray に新しい機能を追加することです。この新しい機能とは、配列の各要素が 10 未満である場合にエラーメッセージを返すバリデーションです。これを実現するために、validateDecorator というデコレータ関数を定義し、既存の sumOfArray 関数をラップしてください。

デコレータパターンを使用することで、ソースコードを修正することなく既存の関数に新しい振る舞いを追加することができます。これにより、既存の関数の基本構造を変更することなく機能を拡張し、コードの重複を減らし、コードベースの保守性を向上させることができます。

テストケース

sum = validateDecorator(sumOfArray)

sum([10,20,30,40]) --> Sum of array is 100

sum([9,10,20,30]) --> 1 error found

sum([3,5,40,50]) --> 2 error found
"""

def validateDecorator(f):
    def function(arr):
        result = f(arr)
        count = 0
        for i in arr:
            if i < 10:
                count += 1
        if count > 0:
            return str(count) + " error found"
        else:
            return "Sum of array is " + str(result)

    return function

def sumOfArray(arr):
    result = 0
    for i in arr:
        result += i
    return result



sum = validateDecorator(sumOfArray)
print(sum([10,20,30,40])) #--> Sum of array is 100
print(sum([9,10,20,30])) #--> 1 error found
print(sum([3,5,40,50])) #--> 2 error found

