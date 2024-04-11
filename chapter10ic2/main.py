class MyException(BaseException):
    def __init__(self,message):
        self.message = message

class FiveException(MyException):
    pass

class SevenException(MyException):
    pass

class TenException(MyException):
    pass


try:
    for i in range(10):
        #if i == 5:
            #raise FiveException("5 found")

        if i == 7:
            raise SevenException("found 7")

        if i == 10:
            raise TenException("ten found")

except SevenException as e:
    print(e.message)
except TenException as e:
    print(e.message)
except FiveException as e:
    print(e.message)
else:
    print("nothing found")
finally:
    print('this will always print')




