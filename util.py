#constants
INT = int
STR = str
FLOAT = float

def isint(var) -> bool:
    """ simple function which checks if 'var' is an int"""
    try:
        int(var)
        return True
    except ValueError:
        return False
def isdecimal(var) -> bool:
    """ simple function which checks if 'var' is a decimal number"""
    try:
        float(var)
        return True
    except ValueError:
        return False

def rinput(msg:str,valuetype):
    """ an upgrade of the normal input funtion.

        You can tell rinput via 'valuetype' which kind of value are allowed
        or expected.
        
        Parameters
        ----------
        msg : str
            The question you are asking the user
        valuetype :
            The type of expected value to the question.
            Valid valuetype are:
            STR
            INT
            FLOAT
    """
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

def optionmenue(*options:str,titel:str="",prefix:str=">",exit_:int=0) -> int:
    """ creates a command-line menue with an titel and options and return the number of choice.

        Parameters
        ----------
        options : str
            Options which are going to be showed.
            Multiple options can be added.
            This looks like:
            [1] Option 1
            [2] Option 2
            ...
        titel : str , optional
            Titel which is gonna be displayed above the options.
            Is empty by default, so a title won't show up.
        prefix : str , optional
            Symbol which shows up, when you are asked for an input.
            Default is '>'.
        exit_ : int , optional
            the number which can be entered to exit the optionmenue.
            returns None, if exits this way

        """
    if titel != "":
        print(titel)
    i = 1
    for option in options:
        print("[{}] {}".format(i,option))
        i+=1
    print("Please enter your number of choice, or enter 0 to exit:")
    while True:
        choice = rinput(prefix,INT)
        if exit_ == choice:
            break
        if choice >= 1 and choice <= (i-1):
            return choice
        else:
            print("Input was not valid. Try again!")
