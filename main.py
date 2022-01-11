from menu import Menu

pg_user = "postgres" #postgre user
pg_password = "root" #postgre password
pg_port= "5432" #server port
pg_database= "" #database name

def main():#main function
    mainMenu = Menu()#defines a menu instace
    mainMenu.start()#Calls a start menu

if __name__ == '__main__':
    main()