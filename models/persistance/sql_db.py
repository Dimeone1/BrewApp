import pymysql

class DBHandler():
    def __init__ (self,host = "localhost", port = 33066, user = "root", word = "password" , db = "brew_app_db", name = "DBHandler"):
        self.host = host
        self.port = port
        self.user = user
        self.word = word
        self.db = db
    
    def fetchAllResults(self, table="drink"):

        connection = pymysql.connect(
            self.host,
            self.port,
            self.user,
            self.word,
            self.db
        )
        cursor = connection.cursor()
        cursor.excute(f"SELECT * FROM {table}")
        results = cursor.fetchall()
        if len(results) !=0:
            for result in results:
                for atribute in result:
                    print(atribute)
        else:
            print("No Results Found in table")
