y = input('Enter a number 1-3 :' )
file = open("exercise.txt")
if y == "1":
    print(file.readline())
if y == "2":
    print(file.readline())
    print(file.readline())
if y == "3":
    print(file.readline())
    print(file.readline())
    print(file.readline())
file.close()


z = input('Enter a number 1-3 :')
zile = open("exercise.txt")
run = 0
while True:
    run=run+1
    line = zile.readline()
    if not line:
        break
    if run == 1 and z == '1':
        print(line)
    if run == 2 and z == '2':
        print(line)
    if run == 3 and z == '3':
        print(line)
zile.close()

