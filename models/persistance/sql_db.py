import pymysql

class DBHandler():
    def __init__ (self,host = "localhost", port = 33066, user = "root", word = "password" , db = "brew_app_db", name = "DBHandler"):
        self.host = host
        self.port = port
        self.user = user
        self.word = word
        self.db = db
      
    def addResultToTable(self, table, attributes, values):

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
                sqlstring +=f'"{val}")'
            else:
                sqlstring +=f'"{val}", '

        print("DEBUG: SQL string after values add: " + sqlstring)
        connection = pymysql.connect(
            host = "localhost",
            user = "root",
            password = "password",
            database = "ETL",
            port = 33066,
            autocommit = True
        )
        print("Connection with database established")
        cursor = connection.cursor()
        print("Cursor established")
        cursor.execute(sqlstring)
        print("Executing SQL string")
        cursor.close()
        print("closing cursor")
        connection.close()
        print("closing database connection")
    
    def fetchAllResultsFromTable(self, table):
        sqlstring = f"SELECT * FROM {table}"
        connection = pymysql.connect(
            host = "localhost",
            user = "root",
            password = "password",
            database = "ETL",
            port = 33066,
            autocommit = True
        )
        print("Connection with database established")
        cursor = connection.cursor()
        print("Cursor established")
        cursor.execute(sqlstring)
        print("Executing SQL string")
        results = cursor.fetchall()
        cursor.close()
        print("closing cursor")
        connection.close()
        print("closing database connection")
        return results

    def fetchSingleResultFromTable(self,table,targetval,targetatt):
        sqlstring = f"SELECT * FROM {table} WHERE {targetval} = {targetatt}"
        connection = pymysql.connect(
            host = "localhost",
            user = "root",
            password = "password",
            database = "ETL",
            port = 33066,
            autocommit = True
        )
        print("Connection with database established")
        cursor = connection.cursor()
        print("Cursor established")
        cursor.execute(sqlstring)
        print("Executing SQL string")
        results = cursor.fetchall()
        cursor.close()
        print("closing cursor")
        connection.close()
        print("closing database connection")
        return results


