import pandas as pd
def get_names(filename):
    print(f"Getting names from {filename}")
    names = []
    results = pd.read_csv(filename)

    #convert CS records into dataframe
    temp = results['Name'].tolist()

    for name in temp:
        names.append(name.title())

    return names