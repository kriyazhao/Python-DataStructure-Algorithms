
#-----------------------------------------------------------------
# Define a recursive function to sum up numbers in the list
def listSum(numList):
    if len(numList) == 1:
        return numList[0]
    else:
        return numList[0] + listSum(numList[1:])

print listSum([1, 2, 3, 7, 8, 10])

#-----------------------------------------------------------------
# Define a recursive function to compute the factorial of a number
def calFactorial(num):
    if num == 0:
        return 1
    else:
        return num * calFactorial(num - 1)

print calFactorial(10)

#-----------------------------------------------------------------
# Define a recursive function to compute the factorial of a number
def calFibonacci(num):
    if num == 0:
        return 0
    elif num == 1 or num == 2:
        return 1
    else:
        return calFibonacci(num - 1) + calFibonacci(num - 2)

print calFibonacci(20)

#-----------------------------------------------------------------
# Define a recursive function to convert an integer to a
# string in any base
def toStr(num, base):
    baseString = "0123456789ABCDEF"
    if num < base:
        return baseString[num]
    else:
        return toStr(num // base, base) + baseString[num % base]

print toStr(1245, 10)

#-----------------------------------------------------------------
# Define a recursive function to reverse an input string
def revStr(inputStr):
    if len(inputStr) <= 1:
        return inputStr
    else:
        return inputStr[-1] + revStr(inputStr[:-1])

print revStr("123ABC")

#-----------------------------------------------------------------
# Define a recursive function to check palindrome
def palChecker(inputStr):
    negStr = ",.;- "
    if len(inputStr) == 1:
        print "there are only one char left"
        return True
    elif len(inputStr) == 2:
        if (inputStr[0] == inputStr[1]) or (inputStr[0] in negStr) or (inputStr[1] in negStr):
            print "there are only two char left, they match!"
            return True
        else:
            print "there are only two char left, they don't match!"
            return False      
    else:
        if inputStr[0] in negStr:
            print "top char contains neglected punctuation"
            return (inputStr[1] == inputStr[-1]) and palChecker(inputStr[2:-1])
        elif inputStr[-1] in negStr:
            print "bottom char contains neglected punctuation"
            return (inputStr[0] == inputStr[-2]) and palChecker(inputStr[1:-2])
        elif (inputStr[0] in negStr) and (inputStr[-1] in negStr):
            print "both top and bottom chars contain neglected punctuation"
            return (inputStr[0] == inputStr[-2]) and palChecker(inputStr[2:-2])
        else:
            print "compare top and bottom chars"
            return (inputStr[0] == inputStr[-1]) and palChecker(inputStr[1:-1])

print palChecker("12 345 4321")
print palChecker("aibohphobia")
print palChecker("reviled did I live, said i, as evil I did deliver")
print palChecker("Kanakanak - a town in Alaska")
print palChecker("12 345 321")
