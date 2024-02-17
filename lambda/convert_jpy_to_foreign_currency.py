"""
為替
easy
日本円を他の国の通貨に変換するツールを作成しています。このツールは convertJPYtoForeignCurrency という関数を通じて実装され、その関数は特定の通貨単位を引数として受け取り、日本円からその通貨への変換を行うクロージャを返します。

クロージャは通常の関数と異なり、それが定義されたスコープにある変数を覚えており、そのスコープが消えた後でもそれら変数にアクセスできる特性を持っています。クロージャを使用することで、グローバルスコープに変数を露出させることなく、必要なデータ（通貨単位と換算率）を関数内にカプセル化し、再利用性とコードの安全性を高めます。

他の通貨への換算は、以下を使用してください。また、小数点以下切り捨てで計算してください。

"USD": 135
"EUR": 150
"GBP": 170

テストケース

doller = convertJPYtoForeignCurrency("USD")
doller(10000) --> JPY: 10000 => USD: 74
euro = convertJPYtoForeignCurrency("EUR")
euro(10000) --> JPY: 10000 => EUR: 66
pound = convertJPYtoForeignCurrency("GBP")
pound(10000) --> JPY: 10000 => GBP: 58
"""

def convertJPYtoForeignCurrency(unit):
    convertList = {
        "USD": 135,
        "EUR": 150,
        "GBP": 170
    }

    def f(yen):
        rate = convertList[unit]
        ans = int(yen / rate)
        return "JPY: " + str(yen) + " => " + unit + ": " + str(ans)

    return f



doller = convertJPYtoForeignCurrency("USD")
print(doller(10000)) #--> JPY: 10000 => USD: 74
euro = convertJPYtoForeignCurrency("EUR")
print(euro(10000)) #--> JPY: 10000 => EUR: 66
pound = convertJPYtoForeignCurrency("GBP")
print(pound(10000)) #--> JPY: 10000 => GBP: 58
