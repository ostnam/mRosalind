# this is my first program where I implement a monte-carlo method
from random import randint
k = int(input("k? "))
m = int(input("m? "))
n = int(input("n? "))
nb_of_individuals = k + m + n
nb_of_sims = 1000000
result = 0
population = []
[population.append("homodom") for i in range(k)]
[population.append("hetero") for i in range(m)]
[population.append("homorec") for i in range(n)]

for i in range(nb_of_sims):
    x = randint(0, nb_of_individuals - 1)
    y = randint(0, nb_of_individuals - 1)
    while x == y:
        y = randint(0, nb_of_individuals - 1)
    if "homodom" in (population[x], population[y]):
        result += 1
    elif "hetero" in (population[x], population[y]):
        if "homorec" in (population[x], population[y]):
            roll = randint(0, 1)
            if roll == 0:
                result += 1
        else:
            roll = randint(0, 3)
            if roll != 3:
                result += 1
    print(str(i * 100/nb_of_sims) + "% done")

print(result / nb_of_sims)

