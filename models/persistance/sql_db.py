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
        length = len(attributes)-1
        for index, att in enumerate(attributes):
            if index == length:
                sqlstring +=f"{att})"
            else:
                sqlstring +=f"{att}, "

        print("DEBUG: SQL String after column add: " + sqlstring)

        length = len(values)-1
        sqlstring += " VALUES ("
        for index, val in enumerate(values):
            if index == length:
                sqlstring +=f'"{val}")'
            else:
                sqlstring +=f'"{val}", '

        print("DEBUG: SQL string after values add: " + sqlstring)
        connection = pymysql.connect(
            host = self.host,
            user = self.user,
            password = self.word,
            database = self.db,
            port = self.port,
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
            host = self.host,
            user = self.user,
            password = self.word,
            database = self.db,
            port = self.port,
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
            host = self.host,
            user = self.user,
            password = self.word,
            database = self.db,
            port = self.port,
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

    def fetchSingleColumnFromTable(self, table, target):
        sqlstring = f"SELECT DISTINCT {target} FROM {table}"
        connection = pymysql.connect(
            host = self.host,
            user = self.user,
            password = self.word,
            database = self.db,
            port = self.port,
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

    def fetchJoinedResultFromTable(self, table, targetval, targetatt, joinedTables = []):
        sqlstring = f"SELECT * FROM {table} WHERE {targetval} = {targetatt} \n"

        for x in joinedTables:
            sqlstring +="INNER JOIN "
            for tableInfo in x:
                jointable = tableInfo[0]
                tableKey = tableInfo[1].get("key")

                sqlstring += f"{jointable} ON {table}.{tableKey}={jointable}.{tableKey} \n"

        connection = pymysql.connect(
            host = self.host,
            user = self.user,
            password = self.word,
            database = self.db,
            port = self.port,
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



