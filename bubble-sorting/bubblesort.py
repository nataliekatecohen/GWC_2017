import random

num = int(input("How many numbers would you like? "))

randnum = []

for rand in range(num):
    randnum.append(int(input("What number would you like in your list? ")))

print(randnum)

for rand in range(len(randnum)-1,0,-1):
    for i in range(rand):
        if randnum[i] > randnum[i+1]:
            temp = randnum[i]
            randnum[i] = randnum[i+1]
            randnum[i+1] = temp

print(randnum)
