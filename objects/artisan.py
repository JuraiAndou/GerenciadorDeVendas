class Artisan(object):
    @property
    def cpf(self):
        return self._cpf
    
    @cpf.setter
    def cpf(self, cpf):
        self._cpf = cpf

    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, name):
        self._name = name

    @property
    def contact(self):
        return self._name

    @contact.setter
    def contact(self, contact):
        self._contact = contact