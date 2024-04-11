
# importing customer class from file


from customer import Customer
# creating customer class


def readCustomers():
    # initialize the array for the customers to be read to
    customers = []
    try:
        # open txt file for reading
        with open('input.txt', 'r') as handle:
            # skip first line
            handle.readline()
            # strip each line from text file into csv format
            for line in handle:
                accountNumber, amount = line.strip().split(':')
                # add each line into the customer array
                customers.append(Customer(accountNumber, float(amount)))
    except Exception as E:
        print(E)
    # returns the array
    return customers


# declare main method
def main_method():
    # executes the method readCustomers and copies the array to another variable
    customers = readCustomers()
    # reads each entry
    for x in customers:
        # executed the method from customer file for each
        x.calculateInterestPayment()
    try:
        # opens a writeable file and and gives it a name
        with open('output.csv', 'w') as file:
            # writing a title line
            file.write('Account #,Amount\n')
            # write the elements in array to csv format
            for x in customers:
                file.write(f'{x.accountNumber}, {x.amount}\n')
    except Exception as E:
        print("Error")

# executing main method


if __name__ == '__main__':
    main_method()