#constants
INT = int
STR = str
FLOAT = float

def isint(var):
    try:
        i = int(var)
        return True
    except ValueError:
        return False
def isdecimal(var):
    try:
        i = float(var)
        return True
    except ValueError:
        return False

def rinput(msg,valuetype):
    if valuetype == str:
        return input(msg)
    elif valuetype == int:
        while True:
            inp = input(msg)
            if isint(inp):
                return int(inp)
            print("Input was not valid. Try again!")
    elif valuetype == float:
        while True:
            inp = input(msg)
            inp = inp.replace(",",".")
            if isdecimal(inp):
                return float(inp)
            print("Input was not valid. Try again!")
    else:
        print("Wrong 'valuetype'. Use 'STR','INT' or 'FLOAT'")

