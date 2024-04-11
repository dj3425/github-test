def phase1():
    # creates the list to store cc numbers
    creditCardsNums = []
    # sends instruction message to user
    print("Phase 1: Enter three unique credit card numbers.")
    # runs loop for cc input if the amount of entries in array is less than 3 cc
    while len(creditCardsNums) < 3:
        try:
            # input statement into formula to be tested
            cc = input(f'enter your credit card number {len(creditCardsNums) + 1}:')
            # checks if cc number is already in the array
            if cc in creditCardsNums:
                # prints error for duplicate cc number
                print('you have already entered this card number')
            else:
                # if not a duplicate cc, add to list
                creditCardsNums.append(cc)
                # prints exception for errors for values
        except Exception as e:
            print("error occurred on cc ")
    # returns the list completely to be ready for next method
    return creditCardsNums


def phase2(cc):
    # creates a list for validating each number
    validate = []
    # analyzes each cc number in the list
    for i in cc:
        ''' validates if the number starts with a 4,5,or 6 and appends, if not, it sends 
        error message for invalid number and which card'''
        if len(i) == 16 and i.isdigit() and i[0] in ['4', '5', '6']:
            validate.append(i)
        else:
            # used because I wanted to be able to tell which cc number that was entered was the one incorrect
            print(f"The number {i} was not valid and was removed.")
            # returns the valid array to the valid list
    return validate


# formats each valid cc number in the list and prints the list our
def phase3(validate):
    print("Phase 3: Valid credit card numbers formatted with dashes.")
    for number in validate:
        formattedNumber = '-'.join([number[i:i + 4] for i in range(0, 16, 4)])
        print(formattedNumber)

#combines all phases/methods into opne method so that they can be done at once dynamically
def main():
 # instead of splitting them up, this means we aren"t doing the first function and possibly not doing the whole thing before
    # we try doing the first method again and writing over the old data
    creditCardNumbers = phase1()
    validNumbers = phase2(creditCardNumbers)
    phase3(validNumbers)

#calls the main method
main()