class SquareRootError(Exception):
    pass

def squareRoot(x):
    if x == 0: return 0

    # 例外をインスタンスオブジェクトとしてメッセージと共に渡すこともできます。
    # これはキャッチされたときに使われ、具体的に何が起こったのかについてより多くの情報を提供する必要があります。
    if x < 0: raise SquareRootError(f"Square root error for the squareRoot function, line 17!!! This function cannot contain a negative integer and {x} was passed in!")

    def isSquareRootCloseEnough(a, b):
        return abs(a / b - b) < (b * 0.000001)

    def squareRootHelper(x, guess):
        if isSquareRootCloseEnough(x, guess):
            return round(guess,5)
        return squareRootHelper(x, (guess + x / guess) / 2)

    return squareRootHelper(x, 1)


print(squareRoot(65))
print(squareRoot(4))
print(squareRoot(25))
print(squareRoot(16))
print(squareRoot(36))
print(squareRoot(353))

# try-catch文の周りで、例外エラーを返す可能性があるステートメントをラップします。
# Pythonではcatchの代わりに「except」というキーワードが使われます。except {ExceptionName}.

# tryの中で以下の文を実行してみてください。
try:
    print(squareRoot(-9))  # ERROR

# tryに失敗した場合は例外をキャッチします。
# キャッチしようとしているのはSquareRootErrorです。制御フローはこのインスタンスオブジェクトを作成して、errに割り当てます。
except SquareRootError as err:
    # エラーは発生しません。試したステートメントが重要ではないことがわかります。
    # 致命的なエラーを起こさずに、起きたことをログ情報にして、プログラムを実行し続けます。
    print("Error occured and it looks like it was a SquareRootError..." + str(err))

print(squareRoot(90))
print(squareRoot(81))
print(squareRoot(54442))

try:
    print(squareRoot(-456))  # ERROR
# また、SquareRootErrorをキャッチして他のすべてのエラーを致命的なエラーにするのではなく、すべての例外を意味する汎用的な例外をキャッチすることもあります。
except Exception as err:
    print("Error occured and it looks like it was an... I am not sure, this is a generic exception with the message:" + str(err))
