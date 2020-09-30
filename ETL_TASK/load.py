import pymysql

def connectToDB(sql_query):
    print("Connecting to database at localhost:8080")

def addToDB(records):
    print("Adding records to database")

    for item in records:
        fname = item.get("fname")
        sname = item.get("sname")

        record = [fname,sname]
        attr = ["fname", "sname"]

        addResultToTable(attr,record,"ETL")


def addResultToTable(attributes, values, table):

        sqlstring = f"INSERT INTO {table} ("

        for att in attributes:
            if att == attributes[-1]:
                sqlstring +=f"{att})"
            else:
                sqlstring +=f"{att}, "

        print("DEBUG: SQL String after column add: " + sqlstring)

        sqlstring += " VALUES ("
        for val in values:
            if val == values[-1]:
                sqlstring +=f"{val})"
            else:
                sqlstring +=f"{val}, "

        print("DEBUG: SQL string after values add: " + sqlstring)
        connection = pymysql.connect(
            host = "localhost",
            user = "root",
            password = "password",
            database = "ETL",
            port = 8080,
            autocommit = True
        )
        print("Connection with database established")
        cursor = connection.cursor()
        print("Cursor established")
        cursor.execute(sqlstring)
        connection.commit()
        print("Executing SQL string")
        cursor.close()
        print("closing cursor")
        connection.close()
        print("closing database connection")