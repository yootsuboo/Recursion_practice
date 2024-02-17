import math

class LambdaMachine:
    def __init__(self):
        self.handlers = {}
    
    def insert(self, key, func):
        self.handlers[key] = func
    
    def retrieve(self, key):
        return self.handlers[key]

  
pythagora = lambda x, y: math.floor(math.sqrt(x**2 + y**2))
addition = lambda x, y: x + y
multiplication = lambda x, y: x * y



lambdaMachine = LambdaMachine()
lambdaMachine.insert("pythagora", pythagora)
print(lambdaMachine.retrieve("pythagora")(3,4)) #--> 5
lambdaMachine.insert("addition", addition)
print(lambdaMachine.retrieve("addition")(2,5)) #--> 7
lambdaMachine.insert("multiplication", multiplication)
print(lambdaMachine.retrieve("multiplication")(4,10)) #--> 40

"""
Lambda Machine
easy
Lambda Machine というデータ構造を作成してください。このデータ構造は、異なる操作を行うラムダ関数と、それに関連する文字列（関数名）を管理し、必要に応じて呼び出せるように設計されています。例えば、加算を行うラムダ関数 addition と、それに関連する文字列 "addition" を入力として受け取り、内部のハンドラ（連想配列）に格納します。関数を使用する際には、関連する名前（例："addition"）を指定して呼び出すことで、対応する操作（この場合は加算）を実行できます。

Lambda Machineは、以下の機能を持ちます。

- array handlers
文字列をキーとし、ラムダ関数を値とする連想配列。

- void insert(String key, callable function)
関数名を表すキーと、関数を実行するラムダ関数をペアとしてデータ構造に挿入します。

- callable retrieve(string key)
キー（関数名）を受け取り、ハッシュマップにペアとしてマップされたラムダ関数を返します。

以下の整数 x、y を受け取り特定の値を返すラムダ関数を作成して、データ構造に挿入してみましょう。

- int pythagora(int x, int y)
直角三角形の 2 辺の長さを x、y とし、斜辺の長さを返すラムダ関数。出力は小数点を切り捨ててください。

- int addition(int x, int y)
x と y を足した値を返すラムダ関数。

- int multiplication(int x, int y)
x と y を掛けた値を返すラムダ関数。
"""
