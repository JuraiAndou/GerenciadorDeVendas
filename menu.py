class Menu(object):
    #Opitions menu class
    def __init__(self):
        pass

    def start(self):
        #Start Menu
        print("======================================")
        print("------------|S.I.V. v1.0|-------------")
        print("======================================")
        print("--------------------------------------")
        print("[1]\tCadastro De Atesã(o)")
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
            cmd = int(input(":"))
            if cmd  == 0:
                exit()
        except Exception as e:
            print(e)
            print("***SOMENTE NUMEROS!!!***")
            self.start()