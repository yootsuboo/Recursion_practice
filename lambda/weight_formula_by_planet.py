def weightFormulaByPlanet(planet):
    accelerationOfGravity = 0
    if planet == "Earth":
        accelerationOfGravity = 9.8
    elif planet == "Mars":
        accelerationOfGravity = 3.7
    elif planet == "Jupiter":
        accelerationOfGravity = 24.8
    return lambda weight: f'The weight on {planet} is {str(int(weight * accelerationOfGravity))}'


getWeightOnEarth = weightFormulaByPlanet("Earth")
print(getWeightOnEarth(50))

getWeightOnMars = weightFormulaByPlanet("Mars")
print(getWeightOnMars(70))

getWeightOnJupiter = weightFormulaByPlanet("Jupiter")
print(getWeightOnJupiter(90))
