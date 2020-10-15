import weakref

class Round():
    _instances = set()
    def __init__ (self, title=""):
        self.title = title
        self._instances.add(weakref.ref(self))
        self.round_data = []

    #store instances of round
    @classmethod
    def get_instances(Round):
        dead = set()
        for ref in Round._instances:
            obj = ref()
            if obj is not None:
                yield obj
            else:
                dead.add(ref)
            Round._instances -=dead    

    def get_round_data(self):
        return self.round_data

    def get_brewer(self):
        return self.brewer
    
    def create_order(self, person , drink):

        order = {"PID": person, "DID": drink}
        self.round_data.append(order)

    def assign_brewer(self):
        is_valid = False
        while True:
            person = input ("Please enter the ID of the desired brewer")
            try:
                person = int(person)
                break
            except ValueError:
                print("Please Enter a valid ID for the brewer")
        while is_valid == False:
            for x in self.round_data:
                print(x.get('PID')== person)
                if x.get("PID") == person:
                    person = int(person)
                    is_valid = True
                    break
            if is_valid == False:
                tmp = input("The name of the brewer must also be present in the round, press 0 to cancel adding a brewer")
                if tmp == "0":
                    break          
        self.brewer = person