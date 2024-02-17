import re

USDtoJPY = 138.31

def calcDollarSalary(baseSalary, hourWage):
    salary = baseSalary

    def getSalary():
        return "$" + str(salary)

    def work(time):
        nonlocal salary
        salary += hourWage * time

    return {
        "getSalary": getSalary,
        "work": work
    }

mikeSalary = calcDollarSalary(100, 12)
mikeSalary["work"](10)
mikeSalary["work"](3)
print("Mike's income: " + mikeSalary["getSalary"]())

def changeToYenUnit(f):
    def inner():
        USDtoJPY
        moneyWithUnit = f()
        result = re.findall(r'\d+.?\d*', moneyWithUnit)[0]
        yenUnitMoney = float(result)  * USDtoJPY
        return "en" + str(yenUnitMoney)
    return inner

ryoSalary = calcDollarSalary(80, 10)
ryoSalary["work"](10)
ryoSalary["work"](6)
print("Ryo's income: " + ryoSalary["getSalary"]())

getRyoSalaryYen = changeToYenUnit(ryoSalary["getSalary"])
print("Ryo's income(yen): " + getRyoSalaryYen())

print("--------")
mikeSalary["work"](19)
ryoSalary["work"](28)

print("Mike's income: " + mikeSalary["getSalary"]())
print("Ryo's income: " + ryoSalary["getSalary"]())

print("Ryo's income(yen): " + getRyoSalaryYen())
