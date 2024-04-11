def funct1(a=100,b=200,c=300):
    print(b)




funct1(a=500)
funct1(b=500)

def sumnat(*nums):
    sum=0
    for number in nums:
        sum=sum+number
    print(sum)

def sumnation(**ums):
    print(ums)
    print(ums["a"])


sumnat(6,39,2929,29,2,9)

sumnation(g=2,b=3,f=8,c=999,a=852)

def sumnation2(*numbs):
    total=0
    for i in numbs:
        total=total+i
    return total

print(sumnation2(1,2,3,4,5,6,7))

import game
roll=game.diceroll()
print(roll)