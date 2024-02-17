# 'simpleDecorator'というデコレータ関数を定義します。この関数は他の関数 'f' を引数として取ります。
def simpleDecorator(f):
    # 'simpleDecorator'関数は内部で 'inner' 関数を定義します。この 'inner' 関数は元の関数 'f' をラップ（包む）します。
    def inner():
        # 'inner' 関数はまず、"Running f......"というメッセージを表示します。これが追加する新たな機能です。
        print("Running f......")

        # そして元の関数 'f' を呼び出し、その結果を返します。
        return f()

    # 最後に 'inner' 関数を実行した結果を返します。
    return inner()

# 'helloWorld'というシンプルな関数を定義します。この関数は "Hello world" という文字列を返します。
def helloWorld():
    return "Hello world"

# 'simpleDecorator'関数を使って 'helloWorld'関数に新たな機能（コンソールにメッセージを表示する）を追加します。
# 結果は 'newFunc1' という新しい関数として保存します。
newFunc1 = simpleDecorator(helloWorld)

# 'newFunc1'関数を実行します。これにより "Running f......" と表示され、その後 "Hello world" が表示されます。
print(newFunc1)

# 'simpleDecorator'関数を使って無名関数（ラムダ関数）に新たな機能を追加します。この無名関数は "Hello Jupiter" を返します。
# 結果は 'newFunc2' という新しい関数として保存します。
newFunc2 = simpleDecorator(lambda : "Hello Jupiter")

# 'newFunc2'関数を実行します。これにより "Running f......" と表示され、その後 "Hello Jupiter" が表示されます。
print(newFunc2)
