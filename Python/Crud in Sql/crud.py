import mysql.connector

class crud:
    def __init(self, host, userName, passwd):
        self.host = host,
        self.userName = userName,
        self.passwd = passwd
        
        mydb = mysql.connector.connect(
          host = host,
          userName = userName,
          passwd = pwsswd
            )
        mycursor = mydb.cursor()
        
    def insert(sql_command):
        mycursor.execute(sql_command)
        mydb.commit()
        """"
        #you can also use this syntax for fixing query
        sql = "INSERT INTO customers (name, address) VALUES (%s, %s)"
        val = ("John", "Highway 21")
        mycursor.execute(sql, val)
        """
        print(mycursor.rowcount, "record inserted.")
        
        
    def delete(tbl_name, *args):
        if args:
            sql = f"DELETE FROM {tbl_name} where {args[0]} {args[1]} {args[2]}"
        else:
            sql = f"DELETE FROM {tbl_name}"
            
        mycursor.execute(sql)
        mydb.commit()
        print(mycursor.rowcount, "record(s) deleted")
        
    
    def update(tbl_name, column, new_value, *args):
        if args:
            sql = f"UPADTE {tbl_name} SET {column} = {new_value} WHERE {args[0]} {args[1]} {args[2]} "
        else:
            sql = f"UPADTE {tbl_name} SET {column} = {new_value}"
        mycursor.execute(sql)
        mydb.commit()
        print(mycursor.rowcount, "record(s) affected") 
        
    def selelct(tbl_name, *args):
        if args:
            sql = f"SELECT * FROM {tbl_name} WHERE {args[0]} {args[1]} {args[2]}"
        else:
            sql = f"SELECT * FROM {tbl_name}"
        mycursor.execute(sql)
        result = mycursor.fetchall()

        for  items in result:
            print(items)
            
