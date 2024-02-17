def closure():
   # 関数外部から直接pivateValueにアクセスはできません。
   privateValue = "private"
   
   # inner関数を経由することで取得できます。
   def getPrivateValue():
         return privateValue
      
   # 内部privateValueの値を取得するための関数を返し、データの出入り口を作ります。
   # 関数の戻り値を取得するために"()"はいらない??
   return getPrivateValue
 
closureFn = closure()
 
# 直接関数内の変数にアクセスできません。
# print(closureFn.privateValue)
 
# closureFnから返ってきた関数を実行することで、関数内の変数を取得できます。
print(closureFn())
 
 
# さらに、関数内の変数を取得・編集するinner関数を作成し、
# hashMapなどで複数の関数を返すことにより、関数内の変数・関数へのアクセスを制御することができます。
def createObject():
   # 関数外部から直接pivateValueにアクセスできませんが、
   # 外部に公開したinner関数経由で編集が可能です。
   privateValue = "private"

   # inner関数を経由することで編集できます。
   def setPrivateValue(newValue):
      nonlocal privateValue
      accessAlert()
      privateValue = newValue
   # inner関数を経由することで取得できます。
   def getPrivateValue():
      return privateValue
   
   # inner関数も外部から隠蔽することができます。
   def accessAlert():
      print("data changed!")
   
   # hashMapを使用し、複数の関数を返すことも可能です。
   return {
      "setValue": setPrivateValue,
      "getValue": getPrivateValue
   }

newObj = createObject()
 
# hashMapのキーgetValueから呼び出した関数を実行します。
print(newObj["getValue"]())
 
# 今回はsetValueを実装したため、内部の変数を更新できます。
newObj["setValue"]("newValue")
print(newObj["getValue"]())
 
# また、accessAlert()は外部からは呼べません。
# newObj.accessAlert() -> error
