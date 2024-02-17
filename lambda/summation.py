# 関数summationは数学的にはΣの役割を果たします。
# 具体的には、関数gを適用した結果をaからbまで足し合わせる関数です。
def summation(g, a, b):
   # bがaより小さい場合、再帰の基底条件になり、結果は0を返します。
   if b < a: return 0
   # bがa以上の場合、bに関数gを適用し、それを再帰的にaまでの合計と足し合わせます。
   return g(b) + summation(g, a, b-1)

# lambda関数identityは、入力された値をそのまま返します。 
identity = lambda i: i

# summation関数を使用して、1から10までの整数の合計を計算します。
# 結果: 55
print(summation(identity, 1, 10))

# summation関数を使用して、10を100回足し合わせた結果を計算します。
# 結果: 1000
print(summation((lambda i: 10), 1, 100))

# 関数pPiは数学的にはΠの役割を果たします。
# 具体的には、関数gを適用した結果をaからbまで掛け合わせる関数です。
def pPi(g,a,b):
   # bがaより小さい場合、再帰の基底条件になり、結果は1を返します。
   if b < a: return 1
   # bがa以上の場合、bに関数gを適用し、それを再帰的にaまでの積と掛け合わせます。
   return g(b) * pPi(g, a, b-1)

# pPi関数を使用して、1から10までの整数の積（つまり10の階乗）を計算します。
# 結果: 3,628,800
print(pPi(identity, 1, 10))

# pPi関数を使用して、5を10回掛け合わせた結果を計算します。
# 結果: 9765625
print(pPi((lambda i: 5), 1, 10))
