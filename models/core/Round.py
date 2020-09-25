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
    
    def create_order(self):
        drink = ""
        person = ""
        order = {"drink": drink, "name": person}
        self.round_data.append(order)

    def assign_brewer(self):
        person = input ("Please enter the name of the desired brewer")
        for x in self.round_data:
            for y in x:
                if y.get("name") == person:
                    is_valid = True
        if is_valid:
            self.brewer = person