from ..handlers import TableHandler as TH
from ..core import Round as R
from ..persistance import json_storage as Storage
import os

class Round_Handler():
    ROUNDTABLENAME = "round"
    ROUNDATTRIBUTES = ["RID","PID ", "DID", "BID"]
    def __init__(self, preferences):
        self.previous_rounds = []
        self.Table_Handler = TH.TableHandler("Table_Handler_Rounds")
        self.preferences = preferences

    def get_previous_rounds(self):
        return self.previous_rounds
    
    def add_round_to_manager(self,round):
        self.previous_rounds.append(round)
        os.system("cls")
        print("Creating a new round")

    def update_drink_preferences(self, preferences):
        self.preferences = preferences

    def round_menu(self, SQLDB = None):
        list_of_inputs=["0","1", "2"]
        os.system('cls')
        return_to_menu = False
        while(~return_to_menu):
            print("""Please select an option by using a number
            [1] - Order a new round
            [2] - View Round History (This Session)
            [0] - Back to main menu""")

            menu_in = input("\n")

            if menu_in == list_of_inputs[0]:
                break
            elif menu_in == list_of_inputs[1]:
                finalize_round = False
                new_round = R.Round()
                while finalize_round == False:
                    PID = ""
                    while PID == "":
                        print("Please Enter the ID of the user you would like to add to the round:\n")
                        tmpID = input()
                        try:
                            tmpID = int(tmpID)
                            query = SQLDB.fetchSingleResultFromTable("person", "PID", tmpID)
                        except ValueError:
                            print("Please enter a valid integer")                        
                        if len(query)==1:
                            PID = tmpID
                        else:
                            print("ID doesnt exist in database, please enter a valid ID")
                    DID = ""
                    while DID == "":
                        print("Please Enter the ID of the drink you would like to add to the round:\n")
                        tmpID = input()
                        try:
                            tmpID = int(tmpID)
                            query = SQLDB.fetchSingleResultFromTable("person", "PID", tmpID)
                        except ValueError:
                            print("Please enter a valid integer")                        
                        if len(query)==1:
                            DID = tmpID
                        else:
                            print("ID doesnt exist in database, please enter a valid ID")

                    new_round.create_order(PID, DID)

                    tmp = input("Press any key to add a new entry to the round, press 0 to finalize the round:\n")
                    if tmp == "0":
                        finalize_round = True

                values = []

                new_round.assign_brewer()
                brewer = new_round.get_brewer()
                roundIDS = SQLDB.fetchSingleColumnFromTable(self.ROUNDTABLENAME, self.ROUNDATTRIBUTES[0])
                lastIndex = roundIDS[-1]
                RID = lastIndex[-1]+1
                if brewer is not None:
                    for order in new_round.get_round_data():
                        values = []
                        values.append(RID)
                        values.append(order.get("PID"))
                        values.append(order.get("DID"))
                        values.append(brewer)
                        SQLDB.addResultToTable(self.ROUNDTABLENAME, self.ROUNDATTRIBUTES, values)

            elif menu_in == list_of_inputs[2]:
                previous = self.get_previous_rounds()
                while True:
                    counter = 0
                    while counter <len(previous):
                        while True:                    
                            self.Table_Handler.print_query(previous[counter], f"Round Number [{counter+1} of [{len(previous)+1}")
                            userin = input("Press [1] to view the previous round, Press [2] to view the next round, press any other key to cancel view\n")
                            if userin == "1":
                                counter -=1                      
                                if counter <= 0:
                                    counter = len(previous)-1
                            if userin == "2":
                                counter +=1
                                if counter>= len(previous):
                                    counter = 0
                            else:
                                break
                            
