import sys
from databaseCalls.dbComands import DbCommands

class Menu(object):
    #Opitions menu class
    def __init__(self):
        self.db_commands = DbCommands()

    def start(self):
        #Start Menu
        print("======================================")
        print("------------|S.I.V. v1.0|-------------")
        print("======================================")
        print("--------------------------------------")
        print("[1]\tCadastro De Artesã(o)")
        print("--------------------------------------")
        print("[2]\tCadastro De Produto")
        print("--------------------------------------")
        print("[3]\tAtualizar Estoque")
        print("--------------------------------------")
        print("[4]\tVender")
        print("--------------------------------------")
        print("[5]\tConsultar Vendas")
        print("--------------------------------------")
        print("[0]\tSair")
        print("--------------------------------------")
        try :
            cmd = int(input(":"))#gets user input

            #Tests for commands
            if cmd  == 0:
                sys.exit()#Exits Program
            elif cmd == 1:
                self.art_reg()
            elif cmd == 2:
                self.prod_reg()
            elif cmd == 3:
                self.update_stk()
            elif cmd == 4:
                self.sell()
            elif cmd == 5:
                self.sale_reg()
            else:#invalid command
                print("***COMANDO INVÁLIDO!!!***")
                self.start()
        except Exception as e:
            #invalid command format
            print(e)
            print("***SOMENTE NUMEROS!!!***")
            self.start()
    
    def art_reg(self):#artisan register
        #Start Menu
        print("======================================")
        print("--------|Cadastro De Artesã(o)|-------")
        print("======================================")
        print("--------------------------------------")
        print("[1]\tListar Artesãs(os)")
        print("--------------------------------------")
        print("[2]\tCadastrar Artesã(o)")
        print("--------------------------------------")
        print("[0]\tSair")
        print("--------------------------------------")
        try :
            cmd = int(input(":"))#gets user input

            #Tests for commands
            if cmd  == 0:
                sys.exit()#Exits Program
            elif cmd == 1:
                pass
            elif cmd == 2:
                pass
            else:#invalid command
                print("***COMANDO INVÁLIDO!!!***")
                self.start()
        except Exception as e:
            #invalid command format
            print(e)
            print("***SOMENTE NUMEROS!!!***")
            self.start()

    def prod_reg(self):#product register
        pass

    def update_stk(self):#update stock
        pass

    def sell(self):#sell an item
        pass

    def sale_reg(self):#sale register
        pass