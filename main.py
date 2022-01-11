from menu import Menu

def main():#main function
    print("***Altere suas credeciais no arquivo \'credentials.py\'***")
    #input("enter para prosseguir")
    mainMenu = Menu()#defines a menu instace
    mainMenu.start()#Calls a start menu

if __name__ == '__main__':
    main()