class Student:
    uid = ''
    firstName = 'FirstName'
    lastName = 'LastName'
    birthDate = ''
    diploma = 'no'

    def __init__(self, fName, lName):
        self.firstName = fName
        self.lastName = lName
    def finishCollege(self):
        self.diploma = 'yes'

Bob = Student('Bob', 'Smith')
Lisa = Student('Lisa', 'Smith')
Christie = Student('Christie', 'Smith')

Bob.finishCollege()
Lisa.finishCollege()
Christie.finishCollege()