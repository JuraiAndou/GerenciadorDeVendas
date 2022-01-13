class Product(object):
    @property
    def id(self):
        return self._id
    
    @id.setter
    def id(self, id):
        self._id = id
    
    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, name):
        self._name = name
    
    @property
    def provider(self):
        return self._provider
    
    @provider.setter
    def provider(self, provider):
        self._provider = provider
    
    @property
    def price(self):
        return self._price
    
    @price.setter
    def price(self, price):
        self._price = price