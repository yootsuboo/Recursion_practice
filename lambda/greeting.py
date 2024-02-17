"""
挨拶のルールは以下の通りです。

- time が 0 以上、12 より小さい場合は "Good Morning"
- time が 12 以上、18 より小さい場合は "Good Afternoon"
- それ以外の場合は "Good Evening"

string loud(string text)
text を文字列として受け取り、すべて大文字で返す関数。

string quiet(string text)
text を文字列として受け取り、すべて小文字で返す関数。

string reverse(string text)
text を文字列として受け取り、文字の順序を逆転して返す関数。

string repeat(string text)
text を文字列として受け取り、文字列を 2 回繰り返す関数。

最終的な挨拶メッセージは、選択された時間帯に応じた挨拶と、変換されたテキストを組み合わせたものになります。
"""

def greet(time, name, f):
    greeting = ""
    if 0 <= time < 12:
        greeting = "Good Morning"
    elif 12 <= time < 18:
        greeting = "Good Afternoon"
    else:
        greeting = "Good Evening"
    return greeting + " " + f(name)

loud = lambda text: text.upper() 
quiet = lambda text: text.lower()
reverse = lambda text: text[::-1]
repeat = lambda text: text + " " + text


print(greet(1, "John", loud)) # --> Good Morning JOHN
print(greet(2, "John", quiet)) # --> Good Morning john
print(greet(13, "John", reverse)) # --> Good Afternoon nhoJ
print(greet(19, "John", repeat)) # --> Good Evening John John
print(greet(13, "Leslie Emmanuel Beadon", loud)) # --> Good Afternoon LESLIE EMMANUEL BEADON
print(greet(19, "Leslie Emmanuel Beadon", quiet)) # --> Good Evening leslie emmanuel beadon
print(greet(5, "Leslie Emmanuel Beadon", reverse)) # --> Good Morning nodaeB leunammE eilseL
print(greet(1, "Leslie Emmanuel Beadon", repeat)) # --> Good Morning Leslie Emmanuel Beadon Leslie Emmanuel Beadon

