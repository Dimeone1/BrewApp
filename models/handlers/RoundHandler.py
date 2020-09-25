from ..handlers import TableHandler as TH
from ..core import Round as R
from ..persistance import json_storage as Storage
import os

class Round_Handler():
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

    def round_menu(self):
        list_of_inputs=["0","1", "2"]
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
                new_round = R.Round()
                new_round.create_order()
                new_round.assign_brewer()
                self.add_round_to_manager(new_round)
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
                            
