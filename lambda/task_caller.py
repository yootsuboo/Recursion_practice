"""
タスクリスト
easy
Mike は、一連の ToDo リストの項目が文字列として格納された配列 toDoArr を持っています。Mike の目的は、この配列に格納されている ToDo リストの各項目を順に出力するプログラムをラムダクロージャを使って作成することです。

ラムダクロージャは、関数内で定義された変数の状態を保持する能力を持っています。この特性を利用して、配列の各要素を順番に処理し、関数が再度呼び出されたときに前回の状態（どの要素が最後に出力されたか）を覚えておくことができます。これにより、配列の各要素を一つずつ、連続して出力することが可能になります。

テストケース

todoCaller = todoCall(["Read a Book", "Work out", "Recursion"])

todoCaller() --> Read a Book

todoCaller() --> Work out

todoCaller() --> Recursion

todoCaller() --> All done!
"""

def todoCall(taskList):
    index = 0
    def f():
        nonlocal index
        task = taskList[index] if index < len(taskList) else "All done!"
        index += 1
        return task
    return f


todoCaller = todoCall(["Read a Book", "Work out", "Recursion"])
print(todoCaller()) #--> Read a Book
print(todoCaller()) #--> Work out
print(todoCaller()) #--> Recursion
print(todoCaller()) #--> All done!
