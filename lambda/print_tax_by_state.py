def printTaxByState(state):
    federalTax = 0.21
    stateTax = 0

    if state == "Arizona":
        stateTax = 0.049
    elif state == "California":
        stateTax = 0.088
    elif state == "Northcarolina":
        stateTax = 0.025
    return lambda profit: f'Federal Tax: {int(profit * federalTax)}\n{state} Tax: {int(profit * stateTax)}\nTax Amount: {int(profit * (federalTax + stateTax))}'

getTaxInAZ = printTaxByState("Arizona")
print(getTaxInAZ(400000))
# --> Federal Tax: 84000
# --> Arizona State Tax: 19600
# --> Tax Amount: 103600


getTaxInCA = printTaxByState("California")
print(getTaxInCA(100000))
# --> Federal Tax: 21000
# --> California State Tax: 8800
# --> Tax Amount: 29800


getTaxInNC = printTaxByState("Northcarolina")
print(getTaxInNC(500000))
# --> Federal Tax: 105000
# --> Northcarolina State Tax: 12500
# --> Tax Amount: 117500
