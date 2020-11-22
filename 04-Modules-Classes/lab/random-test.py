#Random - not real random, psuedo-random numbers.
#current time -> * +, / -> number
#Time always goes forward -> 1s, 2s
#Seed, number
#2020202020 -> same result 4,6,7,9
#0 -> same result
#current time -> as seed -> 5, 6, 8
import random
#random function returns a random number between 0 and 1
print(random.random())
print(random.randrange(1, 3))
subjects = ["chemistry", "math", "physics", "biology"]
print(random.choice(subjects))