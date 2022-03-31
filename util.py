import json

#constants
INT = int
STR = str
FLOAT = float

class Utils:
    @staticmethod
    def isint(var) -> bool:
        """ simple function which checks if 'var' is an int"""
        try:
            int(var)
            return True
        except ValueError:
            return False
    @staticmethod
    def isdecimal(var) -> bool:
        """ simple function which checks if 'var' is a decimal number"""
        try:
            float(var)
            return True
        except ValueError:
            return False
    @staticmethod
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
                if Utils.isint(inp):
                    return int(inp)
                print("Input was not valid. Try again!")
        elif valuetype == float:
            while True:
                inp = input(msg)
                inp = inp.replace(",",".")
                if Utils.isdecimal(inp):
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
            choice = Utils.rinput(prefix,INT)
            if exit_ == choice:
                break
            if choice >= 1 and choice <= (i-1):
                return choice
            else:
                print("Input was not valid. Try again!")
    @staticmethod
    def from_Json(json_file):
        try:
            with open(json_file,"r") as f:
                data = json.load(f)
            return data
        except FileNotFoundError as fnf:
            print(f"'{json_file}' was not found!")
            return None
        except IOError as e:
            print(f"There was an IOError:\n{e}")
            return None
        except Exception as e:
            print("There was an unhandeld Exception while using 'from_Json':\n{e}")
    
    @staticmethod
    def from_Json(json_file:str,*args):
        """
        Returns a certain value of a sub element of the json file.

        json_file : str the path to the json file to be read
        *args : any path to the sub element 
        """
        with open(json_file,"r") as f:
            data = json.load(f)
        temp = data
        for item in args:
            temp = temp[item]
        return temp
    
    @staticmethod
    def search_json_for_item(json_string:str,*path_for_search,search_keyword=None,search_value=None):
        """
        Searches for a certain item inside the json_string and returns it, if found

        json_string : str The json string
        *path_for_search : any The path to the level you want to search your item.
                            This should be the level of a list.
        search_keyword : str The keyword you want to search for.
        search_value : any The corresponding value to the keyword you are searching for. 

        returns Item of which your search_keyword is part of; Returns None if there was an Error or search was not successful.- 
        """
        if search_keyword is None and search_value is None:
            return None
        temp = json_string
        try:
            for search_level in path_for_search:
                temp = temp[search_level]
        except KeyError as ke:
            print(f"Could not traverse to your search level!\n{ke}")
            return None
        try:
            for item in temp:
                if item[search_keyword] == search_value:
                    return item
        except KeyError as ke:
            print(f"Could not find the 'search_word'\n{ke}")
            return None
        return None
