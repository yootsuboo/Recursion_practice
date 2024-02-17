"""
複数のデコレータ
medium
この問題の目標は、既存の関数に新しい機能を追加するデコレータを作成し、適用することです。具体的には、文字配列を文字列に変換する toString 関数と、2 つの文字列を連結する concat 関数を作成し、これらの関数に追加機能を提供するデコレータを定義します。

基本関数：

string toString(array arr)
この関数は文字の配列（例：['h','E','L','L','O']）を受け取り、それらを連結して一つの文字列（例："hELLO"）として返します。

string concat(string s1, string s2)
この関数は 2 つの文字列を受け取り（例："Hello" と "World"）、それらを連結して一つの文字列（例："HelloWorld"）として返します。

デコレータパターンにより、開発者はソースコードを修正することなく、既存のオブジェクトに新しい振る舞いを追加することができます。これは既存のオブジェクトの基本構造を変えずに機能を拡張するために非常に便利です。また、デコレータを使用することで、コードの重複を減らし、コードベースの保守性を向上させることが可能です。

実装すべきデコレータ：

callable capitalizeDecorator(callable f)
このデコレータは関数 f を受け取り、新しいラムダ関数を返します。このラムダ関数は、配列の先頭の文字を大文字に変換し（例：['h','E','L','L','O'] が ['H','E','L','L','O'] になる）、その後で関数 f を呼び出して結果の文字列を返します。

callable lowercaseResultDecorator(callable f)
このデコレータは関数 f を受け取り、新しいラムダ関数を返します。このラムダ関数は、関数 f の結果を受け取り、その結果を全て小文字（例："HELLO" が "hello" になる）に変換して返します。

callable printInfoDecorator(callable f)
このデコレータは関数 f を受け取り、新しいラムダ関数を返します。このラムダ関数は、2 つの引数を受け取り（例："HELLO" と "hello"）、それらを関数 f で連結し、加えて連結前の引数を情報（例：f("HELLO", "hello") の結果は "HELLO + hello = HELLOhello" になる）に変換して返します。

テストケース

arr = ['h','E','L','L','O']

f1 = capitalizeDecorator(toString)

f2 = lowercaseResultDecorator(toString)

f3 = printInfoDecorator(concat)

f1(arr) --> HELLO

f2(arr) --> hello

f3(f1(arr),f2(arr)) --> HELLO + hello = HELLOhello
"""

def capitalizeDecorator(f):
    def wrapper(arr):
        arr[0] = arr[0].upper()
        return f(arr)
    return wrapper

def lowercaseResultDecorator(f):
    def wrapper(arr):
        temp = [char.lower() for char in arr]
        return f(temp)
    return wrapper

def printInfoDecorator(f):
    def wrapper(s1, s2):
        return s1 + " + " + s2 + " = " + f(s1, s2)
    return wrapper

def toString(arr):
    return ''.join(arr)

def concat(s1, s2):
    return s1 + s2


arr = ['h','E','L','L','O']
f1 = capitalizeDecorator(toString)
f2 = lowercaseResultDecorator(toString)
f3 = printInfoDecorator(concat)
print(f1(arr)) #--> HELLO
print(f2(arr)) #--> hello
print(f3(f1(arr),f2(arr))) #--> HELLO + hello = HELLOhello
