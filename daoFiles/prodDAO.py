import credentials
import traceback, psycopg2

from objects.product import Product

class ProdDAO(object):
    def __init__(self):
        self._usr = credentials.pg_user
        self._psw = credentials.pg_password
        self._port = credentials.pg_port
        self._db = credentials.pg_database

    def list(self):
        results = []
        try:
            connection = psycopg2.connect(user=self._usr, password=self._psw, port=self._port, database=self._db)
            cursor = connection.cursor()
            cursor.execute("SELECT id, name, provider, price FROM produto")
            registros = cursor.fetchall()
            for r in registros:
                p = Product()
                p.id = r[0]
                p.name = r[1]
                p.provider = r[2]
                p.price = r[3]
                results.append(p)
        except(Exception, psycopg2.Error) as error:
            traceback.print_exc()
        finally:
            if connection:
                cursor.close()
                connection.close()
        return results

    def add():
        pass
    
    def remove():
        pass