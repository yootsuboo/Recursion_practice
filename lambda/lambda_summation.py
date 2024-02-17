# lambda式の結果がTrueならそのときの数字をxに追加する
def summation(f, number):
    x = 0
    for i in range(1, number + 1):
        if f(i):
            x += i
    return x

isOdd = lambda x: True if x % 2 != 0 else False
isMultipleOf3Or5 = lambda x: True if x % 3 == 0 or x % 5 == 0 else False
isPrime = lambda x: all(x % i != 0 for i in range(2, int(x ** 0.5) + 1)) if x > 1 else False



print(summation(isOdd, 3))
print(summation(isOdd, 10))
print(summation(isOdd, 25))
print(summation(isMultipleOf3Or5, 3))
print(summation(isMultipleOf3Or5, 10))
print(summation(isMultipleOf3Or5, 100))
print(summation(isPrime, 2))
print(summation(isPrime, 10))
print(summation(isPrime, 100))


