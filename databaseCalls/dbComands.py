from daoFiles.artDAO import ArtDAO

class DbCommands(object):
    def __init__(self):
        pass

    #Artisan Register
    def list_artisans(self):
        artDAO = ArtDAO()
        artisans = artDAO.list()
        for a in artisans:
            print("*** CPF: "+ str(a.cpf) + " - Nome: " + a.name + " - Contato: " + a.contact + " ***")
        print("*** " + str(len(artisans)) + " cliente(s) cadastrado(s) ***")

    def add_artisan(self, cpf, nome, contato):
        artDAO = ArtDAO()
        success = artDAO.insert(cpf, nome, contato)
        if success:
            print("***Artesã(o) cadastrada(o)***")
        else:
            print("***Erro ao efetuar o cadastro***")