import json
class json_handler():
    def __init__ (self,sf ,name = "json handler"):
        self.storage_file = sf

def save_json(self, data = ""):
    if data == "":
        data = load_json
    try:
        file = open(self.storage_file,"w")
        json.dump(data,file)
        print(f"Saved json to file")
        file.close()
    except Exception as e:
        print(f"Error writing JSON to file {file}\n")
        print(str(e))


def load_json(self):
    filename = self.storage_file
    print(f"loaded json from {filename}")
    data = json.load(open(filename))
    #parse_json(data)
    return data