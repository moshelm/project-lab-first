import mysql.connector


HOST = 'localhost'
PASSWORD = ''
USER = 'root'

class SQLDatabase:
    def __init__(self):
        self.conn = mysql.connector.connect(host=HOST,user=USER)
        self.cursor =  self.conn.cursor()


    def create_database(self, database_name:str):
        self.cursor.execute(f"CREATE DATABASE IF NOT EXISTS `{database_name}`;")


    def create_table(self, database:str, table_name:str):
        self.cursor.execute(f'USE `{database}`')
        self.cursor.execute(f"""CREATE TABLE IF NOT EXISTS `{table_name}` (
                            id INT AUTO_INCREMENT PRIMARY KEY,
                            first\_name VARCHAR(50) NOT NULL,
                            last\_name VARCHAR(50) NOT NULL,
                            phone\_number VARCHAR(20) NOT NULL UNIQUE )
                            
                            ;""")
    

    def insert_contact(self, table_name:str, contact:tuple):
        sql = f"INSERT INTO `{table_name}` (first\_name, last\_name, phon\_number) \
                            VALUES (%s, %s, %s)"
        self.cursor.execute(sql, contact)
        self.conn.commit()



