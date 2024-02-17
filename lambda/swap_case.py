def swapCase(arr):
    print([x.lower() if x.islower() else x.upper() for x in arr ])

swapCase(['l','A','m','b','D','A']) #--> [L,a,M,B,d,a]
swapCase(['a','E','s','P','A']) #--> [A,e,S,p,a]
swapCase(['f','U','N','c','T','I','o','n']) #--> [F,u,n,C,t,i,O,N]

"""
文字のスワップ
easy
文字で構成される配列 charList が与えられるので、大文字は小文字に、小文字は大文字に変換し新しい配列を返す swapCase という関数を map 関数を使用して作成してください。

関数の入出力例

入力のデータ型： char[] charList

出力のデータ型： char[]

swapCase(['l','A','m','b','D','A']) --> [L,a,M,B,d,a]

swapCase(['a','E','s','P','A']) --> [A,e,S,p,a]

swapCase(['f','U','N','c','T','I','o','n']) --> [F,u,n,C,t,i,O,N]
"""
