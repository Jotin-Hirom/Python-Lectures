# a = -5
# if a < 0:
#     raise Exception("Value should be greater than 0.")
# assert(a>=0) , 'Value should be greater than 0.'


# try:
#     a= 5/1
#     c =a + 3
# except Exception as e:
#     print(e)
# except TypeError as e:
#     print(e)
# else:
#     print(a,"Worked.")
# finally:
#     print("Cleaning...")

# Custom Exception
class ValueTooHighError(Exception):
    pass
class ValueTooSmallError(Exception):
    def __init__(self, message, value):
        self.message = message
        self.value = value
def testValue(x):
    if x>100:
        raise ValueTooHighError("Value is too high.")
    elif x < 5:
        raise ValueTooSmallError("Value is very small.", x)
    else:
        print(f"Value of x is {x}")
try:
    testValue(0)
except ValueTooHighError as e:
    print(e)
except ValueTooSmallError as e:
    print(e.value ,e.message )
else:
    print("Worked.")
finally:
    print("Cleaning..")
