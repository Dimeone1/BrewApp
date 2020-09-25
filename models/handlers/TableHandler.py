from ..core import Drink, Person, Round
import unittest

class TableHandler():
    def __init__ (self, name = "Table_Handler"):
        self.name = name
        self.size = 0
        self.padsize = 4
        self.edgechar = "|"
        self.padchar = " "
        self.seperator_string = ""
        self.linechar = "="
        self.capchar = "+"

    #DONE
    def __set_size__(self, title, data):
        if self.size<len(title):
            self.size = len(title)
        for x in data:
            if type(x) == dict:
                for y in x.values():
                    if len(y) > self.size:
                        self.size = len(y)
            elif type(x) == str:
                if len(x) > self.size:
                    self.size = len(x)
            elif type(x) == list:
                for y in x:
                    if len(x[y]) > self.size:
                        self.size = len(x)
        self.size = self.size + self.padsize

    #DONE
    def __padtosize__(self, raw, size = "", is_edge=True):        
        if is_edge:
            string = self.edgechar + raw
        else:
            string = raw
        if size == "":
            size = self.size
        if len(raw)<size-1:
            string += (self.padchar*(size-1-len(raw)))
        if is_edge:
            string +=self.edgechar
        return string

    #NEED to parse input of
        #Lists
            #People - DONE
                #NAME - DONE
                #DRINKPREF - DONE?
            #Drinks - DONE
        #Round - 
        #String - DONE
    #ERROR HANDLING - DONE?
    def __buildstring__(self, raw, key="name"):   
        stringlist = []
        namelist = []
        drinklist = []
        if type(raw) == Round:
            # namelist = [raw.round_data.get("people")]
            # drinklist = [raw.round_data.get("drinks")]
            tempsizecount = 0
            for x in namelist:
                if len(x)>tempsizecount:
                    tempsizecount = len(x)
            for x in namelist:
                stringlist.append(self.edgechar + " Name: " + self.__padtosize__(x, tempsizecount, False))
            for x in drinklist:
                if len(x)>tempsizecount:
                        tempsizecount = len(x)
            for count, x in enumerate(stringlist):
                stringlist[count] += self.edgechar +  " Drink: " + self.__padtosize__(x, tempsizecount, False) + " " + self.edgechar
        elif type(raw) == str:
            return self.__padtosize__(raw, self.size-5)
        elif type(raw) == list:
            if type(raw[0]) == Person or type(raw[0]) == Drink:
                for x in raw:
                    stringlist.append(x.key)
            elif type(raw[0])== dict:
                input("of dicts")
                for x in raw:
                    namelist.append(x.get("name"))
                    drinklist.append(x.get("drink"))
                tempsizecount = 0
                for x in namelist:
                    if len(x)>tempsizecount:
                        tempsizecount = len(x)
                for y in namelist:
                    if len(y)>tempsizecount:
                        tempsizecount = len(y)
                for y in namelist:
                    stringlist.append("Name: " + self.__padtosize__(y, tempsizecount, False))
                for z in drinklist:
                    if len(z)>tempsizecount:
                            tempsizecount = len(z) + 2
                for count, z in enumerate(stringlist):
                    stringlist[count] += self.__padtosize__(" | Drink: " + drinklist[count], tempsizecount + 14, False)
                    stringlist[count] = self.__padtosize__(stringlist[count])
        elif type(raw[0])== dict:
                for x in raw:
                    namelist.append(x.get("name"))
                    drinklist.append(x.get("drink"))
                tempsizecount = 0
                for y in namelist:
                    if len(y)>tempsizecount:
                        tempsizecount = len(y)
                for y in namelist:
                    stringlist.append(self.edgechar + " Name: " + self.__padtosize__(y, tempsizecount, False))
                for z in drinklist:
                    if len(z)>tempsizecount:
                            tempsizecount = len(z) + 2
                for count, z in enumerate(stringlist):
                    stringlist[count] = stringlist[count] + self.edgechar +  " Drink: " + self.__padtosize__(drinklist[count], tempsizecount, False) + " " + self.edgechar

        self.__set_size__("", stringlist)
        return stringlist

    #DONE
    def __print_seperator__(self):
        self.seperator_string = self.capchar
        while len(self.seperator_string)<self.size-5:
            self.seperator_string +=self.linechar
        self.seperator_string +=self.capchar
        print(self.seperator_string)
    
    #DONE
    def __print_line__(self, string):
        print(self.__buildstring__(string))

    #DONE
    def __print_header__(self, title):
        self.__print_seperator__()
        self.__print_line__(title)
        self.__print_seperator__()
    
    #DONE
    def __print_table__(self, lines):    
        for x in lines:
            print(x)
        self.__print_seperator__()

    #DONE
    def print_query(self, data, title=""):
        lines = self.__buildstring__(data)
        self.__print_header__(title)
        self.__print_table__(lines)
