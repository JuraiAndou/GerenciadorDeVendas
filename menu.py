import sys
from databaseCalls.dbComands import DbCommands

class Menu(object):
    #Opitions menu class
    def __init__(self):
        self.db_cmd = DbCommands()

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
                self._art_reg()
            elif cmd == 2:
                self._prod_reg()
            elif cmd == 3:
                self._update_stk()
            elif cmd == 4:
                self._sell()
            elif cmd == 5:
                self._sale_reg()
            else:#invalid command
                print("***COMANDO INVÁLIDO!!!***")
                self.start()
        except Exception as e:
            #invalid command format
            print(e)
            print("***SOMENTE NUMEROS!!!***")
            self.start()
    
#----------------------------------------------------------------------------
    #Artisan Register
    def _art_reg(self):
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
                self.db_cmd.list_artisans()
                input("pressione enter para sair...")
                sys.exit()
            elif cmd == 2:
                self._add_art()
                input("pressione enter para sair...")
                sys.exit()
            else:#invalid command
                print("***COMANDO INVÁLIDO!!!***")
                self._art_reg()
        except Exception as e:
            print(e)
            print("***ERRO***")
            self._art_reg()

    def _add_art(self):
        print("======================================")
        print("---------|Adicionar Artesã(o)|--------")
        print("======================================")
        print("--------------------------------------")
        cpf = input("CPF da(o) artesã(o): ")
        nome = input("Nome da(o) artesã(o): ")
        contato = input("Contato da(o) artesã(o): ")
        self.db_cmd.add_artisan(cpf, nome, contato)

#----------------------------------------------------------------------------
    #Product register
    def _prod_reg(self):#product register
        #Start Menu
        print("======================================")
        print("--------|Cadastro De Produtos|--------")
        print("======================================")
        print("--------------------------------------")
        print("[1]\tListar Produtos")
        print("--------------------------------------")
        print("[2]\tCadastrar Produto")
        print("--------------------------------------")
        print("[3]\tExcluir Produto")
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
            elif cmd == 3:
                pass
            else:#invalid command
                pass
        except Exception as e:
            print(e)
            print("***ERRO***")
            self._art_reg()

    def _add_prod():
        pass
    def _del_prod():
        pass

#----------------------------------------------------------------------------
    #Update Stock
    def _update_stk(self):#update stock
        pass

#----------------------------------------------------------------------------
    #Sell Product
    def _sell(self):#sell an item
        pass

#----------------------------------------------------------------------------
    #Sale Register
    def _sale_reg(self):#sale register
        pass