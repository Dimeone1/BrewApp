import ..ETL_task.extract as extract
import ..ETL_task.transform as transform
import ..ETL_task.load as load

filename = "ETL_TASK/Import_User_Sample_en.csv"


if __name__ == "__main__":
    names = extract.get_names(filename)
    records = []
    print(names)
    for name in names:
        records.append(transform.convert_to_record(name))
    load.addToDB(records)