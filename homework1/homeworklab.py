# Q1 PRINT- declares variables and then prints each line with a string before to give context
v1, v2, v3 = 10, 15, 20
print('var1 =', v1)
print('var2 =', v2)
print('var3 =', v3)
'''Q2 AVERAGE-declares variables, Adds them together, divides by the number of variables which is 5
 (needs to be updated to be dynamic) and then prints each line with a string before to give context'''
g, h, i, j, k = 3, 7, 8, 2, 10
total = g + h + i + j + k
average = total / 5
print('average =', average)

'''Q3 MATH WITH "=" SIGN-declares variable and then does quick math do decrease total input by me, 
and then prints the final line with a string before to give context'''
x = 3
x += 34
x += 22
x += 65
x += 78
x += 99
x -= 44
x -= 33
x -= 22
x -= 11
x *= 5
x *= 4
x *= 3
x *= 2
x *= 1
print("x is", x)

'''Q4 REMAINDER- does math and calculation to find the remainder 
and then prints a line with a string before to give context'''
z = 100 % 23
print("remainder is ", z)

'''Q5 INVESTMENT- declares variables, translates them to nubers that are easier for end user,
 and then prints a string to give the proper information in the right order to give knowledge to end user.'''
name = 'Alice Vahn'
investment = 10000
investment = f'{investment:,}'
interestRate = 0.0532 * 100
print(" %s has invested  $%s into a savings account that has a %4.2f interest rate." % (name, investment, interestRate))

''' Q6   Retirement age- declares variables transforms the string to an integer, adds the variables together 
and then prints each line with a string before to give context'''
retirementAge = '67'
a = 3
retirementAge = int(retirementAge)
a += retirementAge
print("retirement age is now", a)
'''Q7 Grades- declares variables in a list, Adds them together, divides by the number of variables 
 and then prints the average with a string before to give context'''
grades = [90, 89, 93, 75]
total2 = sum(grades)
average2 = total / len(grades)
print("grade average is", average2)
'''Q8 STARWARS- declares an empty dictionary, Adds items, 
and prints out each item by the key name giving the other matching pair'''
starWars = {}
starWars['Han Solo'] = "U123456"
starWars['Luke Skywalker'] = 'U987654'
starWars['Darth Vader'] = 'U876543'
starWars['Ben Kenobi'] = 'U321455'

print(starWars['Han Solo'])
print(starWars['Luke Skywalker'])
print(starWars['Darth Vader'])
print(starWars['Ben Kenobi'])
