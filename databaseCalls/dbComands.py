from daoFiles.artDAO import ArtDAO

class DbCommands(object):
    def __init__(self):
        pass

    #Artisan Register
    def list_artisans():
        pass

    def add_artisan(self, cpf, nome, contato):
        artDAO = ArtDAO()
        success = artDAO.insert(cpf, nome, contato)
        if success:
            print("***Artesã(o) cadastrada(o)***")
        else:
            print("***Erro ao efetuar o cadastro***")