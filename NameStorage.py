
#initial environment setup
import json 
import os
from models.handlers import RoundHandler as RH
from models.handlers import TableHandler as TH
from models.persistance import sql_db as DB

#create initial blank list of dictionaries - filled from JSON later
people_drinks = []

#referenced globally to store various table components
table_size = 0
query_half_size = 0
seperator_string = ""

#table design characters
line_char = "="
cap_char = "+"
edge_char = "|"
pad_char = " "

#SQL DB table names
DRINKTABLENAME = "drink"
DRINKATTRIBUTES = ["name ", "isAlcoholic ", "price "]
PERSONTABLENAME = "person"
PERSONATTRIBUTES = ["fname ", "sname ", "age "]
PREFERENCETABLENAME = "preference"
PREFERENCEATTRIBUTES = ["PID ", "DID "]

#0 for person join, #1 for drink join
JoinedTablesDictList = [["person",{"key": "PID"}],["drink",{"key": "DID"}]]
#JSON storage file
storage_file = "storage.txt"

#list of accepted user command inputs
accepted_commands = ["0","1", "2", "3", "4", "5", "6"]
#set method for table size, potential bad practice

#add a record to the list
def add_record(name, drink):
    #ensure string input
    name = str(name)
    drink = str(drink)
    #create new dictionary
    new_record = {"name":name, "drink":drink}
    people_drinks.append(new_record)
    save_json(people_drinks)


#search through a list to find each record with a matching key value
def search_for_key(key, searchdata, searchlist):
    records = []
    for x in searchlist:
        if key in x:
            #add matching record to return list
            if x.get(key) == searchdata:
                print(f"record found, adding {x.get(key)} to search results")
                records.append(x)
    if len(records) != 0:
        #if at least 1 record was found, return that record - better to return position in initial list?
        return records
    else:
        print(f"No matching records found matching {searchdata} in {key}")



#json test - could add further processing here
def parse_json(rawjson):
    print(rawjson)


#function to edit a users data if there is only a single user with that name  
# def editusersingle(curname,changedval, changekey):
#     #find the occurance of that user
#     for x in people_drinks:
#         if x["name"] == curname:
#             x[changekey] = changedval
#             print(f"Changed key: {changekey} to value: {changedval} in name: {curname}")
#     #update the JSON        
#     save_json(people_drinks)

# def editusersmulti(sr):
#     edited = False
#     while edited == False:
#         #store length of search result list to minimize repeated execution
#         bound = len(search_results)
#         #debug messages, no longer used
#         # print(search_results)
#         # print(f"{bound} users found with that name\n")

#         #clear terminal
#         os.system("cls")
#         #loop until break condition
#         while edited == False:
#             count = 0
#             #unpack search results list
#             for x in sr:
#                 count +=1
#                 name = x.get("name")
#                 drink = x.get("drink")
#                 print(f"[{count}] Name: {name} Favourite drink: {drink}")            
#             print("\n Press the number for the record you would like to edit")        
#             try:
#                 #reduce number by 1 to get correct index
#                 tar = int(input())-1  
#                 if tar<len(search_results) and tar>=0:
#                     tardict = sr[tar]
#                     for y in people_drinks:
#                         #ensure record matches desired record, not just name
#                         if y.get("name") == tardict.get("name"):
#                             if y.get("drink") == tardict.get("drink"):
#                                 print("Record found in main database\n")
#                                 os.system("cls")
#                                 print(f"Editing record name: {y.get('name')} favourite drink {y.get('drink')}")
#                                 while edited == False:
#                                     print("Press [1] if you would like to change the user's name\n [2] if you would like to change their favourite drink\n \nPress any other key to return to the main menu\n")
#                                     tmp = input()
#                                     #change name
#                                     if tmp == "1":
#                                         print("Please input the desired name change\n")
#                                         updated = input()
#                                         y["name"] = updated
#                                         edited =True 
#                                     #change drink   
#                                     elif tmp == "2":
#                                         print("Please input the desired drink change\n")
#                                         updated = input()
#                                         y["drink"] = updated
#                                         edited = True
#                                     #return to menu
#                                     else:
#                                         edited = True
#                                         break
#                 else:
#                     print(f"Please enter a valid search result from between [1] and [{bound}]")   
#             except ValueError:
#                 print("An error has occured, Press any key to refresh search results & ensure your input is only a number")
#                 #print(e)
#                 input()
#     os.system("cls")    
#     save_json(people_drinks)

def save_json(data = "", file = storage_file):
    if data == "":
        data = people_drinks
    try:
        file = open(storage_file,"w")
        json.dump(data,file)
        print(f"Saved json to file")
        file.close()
    except Exception as e:
        print(f"Error writing JSON to file {file}\n")
        print(str(e))


def load_json(filename = storage_file):
    print(f"loaded json from {filename}")
    data = json.load(open(filename))
    #parse_json(data)
    return data

#load previous data from storage file
people_drinks = load_json()
round_handler = RH.Round_Handler(people_drinks)
db_handler = DB.DBHandler()

#begin main method loop
while True:
    #refresh data
    load_json()
    #clear terminal at start of loop
    os.system("cls")

    
    #reset return state
    round_handler.update_drink_preferences(people_drinks)
    table_handler = TH.TableHandler()


    
    # test_search_key_f()
    # test_search_key_s()
    # table_handler.run_tests()
    back_to_menu = False
    #print fresh menu
    print("""Please select an option by using a number
    [1] - View all people  
    [2] - View all drinks 
    [3] - Add a Person
    [4] - Add a Drink
    [5] - Add a Preference
    [6] - Rounds
    [7] - Search for a Person, Drink or Preference
    [0] - Exit""")

    #get command from user
    user_in = input()

    #select function based on user input
    #list existing people
    if user_in == accepted_commands[1]:
        table_handler.print_query(people_drinks, "People")
    #list existing drinks
    elif user_in == accepted_commands[2]:
        table_handler.print_query(people_drinks, "Drinks")
    #add a new record
    elif user_in == accepted_commands[3]:
        print("Please input a first name: \n")
        fname = input()
        print("Please input a surname:\n")
        sname = input()
        age = ""
        while type(age) == str:
            print("Please input the age:\n")
            age = input()
            try:
                age = int(age)
            except ValueError as e:
                print("Error inputting age, please input a numerical value")
        values = [fname,sname,age]

        db_handler.addResultToTable(PERSONTABLENAME, PERSONATTRIBUTES, values)
    #search records
    elif user_in == accepted_commands[4]:
        print("Please input a drink name: \n")
        name = input()
        while True: 
            print("Enter 1 if the drink is alcoholic, enter 0 if it isnt:\n")
            isAlcoholic = input()
            if isAlcoholic == "1":
                isAlcoholic = 1
                break
            elif isAlcoholic == "0":
                isAlcoholic = 0
                break
        price = ""
        while type(price) == str:
            print("Please input the cost of the drink:\n")
            price = input()
            try:
                price = float(price)
            except ValueError as e:
                print("Error inputting price, please input a decimal value")
        values = [name,isAlcoholic,price]

        db_handler.addResultToTable(DRINKTABLENAME, DRINKATTRIBUTES, values)
    #PREFERENCE
    elif user_in ==accepted_commands[5]:
        people = db_handler.fetchAllResultsFromTable(PERSONTABLENAME)
        drinks = db_handler.fetchAllResultsFromTable(DRINKTABLENAME)
        
        prefPID = ""
        while prefPID == "":
            os.system('cls')
            for person in people:
                print(f"PID: {person[0]}")
                for index, atr in enumerate(PERSONATTRIBUTES):           
                    print(f"{atr}: {person[index + 1]}")

            targetID = input("Please Enter a PID for the user you would like to add a preference for: \n")
            try:
                prefPID = int(targetID)
                input(f"Selected ID: {prefPID}, press enter to continue")
            except ValueError:
                print("Please Enter a valid Integer PID. Press enter to select again")

        prefDID = ""
        while prefDID == "":
            os.system('cls')
            for drink in drinks:
                print(f"DID: {drink[0]}")
                for index, atr in enumerate(DRINKATTRIBUTES):
                    print(f"{atr}: {drink[index + 1]}")

            targetID = input("Please Enter a DID for the user you would like to add a preference for: \n")
            try:
                prefDID = int(targetID)
                input(f"Selected ID: {prefDID}, press enter to continue")
            except ValueError:
                print("Please Enter a valid Integer DID. Press enter to select again")

        values = [prefPID, prefDID]  
        db_handler.addResultToTable(PREFERENCETABLENAME, PREFERENCEATTRIBUTES, values)
    elif user_in == accepted_commands[6]:
        round_handler.round_menu(db_handler)
        back_to_menu = True
    elif user_in == accepted_commands[0]:
        save_json(people_drinks)
        parse_json(people_drinks)
        exit()
    else:
        print("Invalid command entered\n")
    if back_to_menu == False:
        input("\nPress any key to return to the main menu\n")
        back_to_menu = True
    os.system("cls")
    save_json()
