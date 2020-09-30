
def convert_to_record(name):
    print(f"Converting {name} to a record")
    tmp = name.split()
    fname = tmp[0]
    sname = tmp[1]
    record = {"fname":fname, "sname":sname}
    print(f"Converted {name} to Record(fname: {fname}, sname: {sname})")
    return record