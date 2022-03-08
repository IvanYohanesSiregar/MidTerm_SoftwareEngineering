import MidTerm
import os
from MidTerm import *


def Menu():
    dbfunc = MidTerm.StudiKasus2

    print("This is the Implementation!")
    print("follow from number 1 until 5, enjoy!\n")
    print("1. Connect Database")
    print("2. Create Database")
    print("3. Load CSV file")
    print("4. Create table ")
    print("5. Load data from database")

    choice = input("Your choice: ")

    def tryConnDB():
        dbfunc._init_(dbfunc, 'host', '3306', 'root', os.environ['PW_DB'])
        dbfunc.connect_db(dbfunc)

    if choice == "1":
        tryConnDB()
        Menu()

    elif choice == "2":
        tryConnDB()
        dbname = input("Input your new database name: ")
        dbfunc.create_db(dbfunc, dbname)
        Menu()

    elif choice == "3":
        tryConnDB()
        path = input("Input the path of CSV file: ")
        dbfunc.import_csv(dbfunc, path)
        print('CSV file imported!\n')
        Menu()

    elif choice == "4":
        tryConnDB()
        dbname = input("Input the name of database: ")
        tbname = input("Input the name of table: ")
        dafe = dbfunc.imp_df()
        print(dafe)
        dbfunc.create_table(dbfunc, dbname, tbname, dafe)
        Menu()

    elif choice == "5":
        tryConnDB()
        dbname = input("Input the name of database: ")
        tbname = input("Input the name of table: ")
        dbfunc.load_data(dbfunc, dbname, tbname)
        
Menu()
        