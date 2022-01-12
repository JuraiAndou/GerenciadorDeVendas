import credentials
import psycopg2
import traceback

from types import TracebackType

from objects.artisan import Artisan

class ArtDAO(object):
    def __init__(self):
        self._usr = credentials.pg_user
        self._psw = credentials.pg_password
        self._port = credentials.pg_port
        self._db = credentials.pg_database
    def insert(self, cpf, name, contact):
        success = False
        try:
            connection = psycopg2.connect(user=self._usr, password=self._psw, port=self._port, database=self._db)
            cursor = connection.cursor()
            cursor.execute("INSERT INTO artesao VALUES (" + cpf + ", \'" + name + "\', \'" + contact + "\' " + ")")
            connection.commit()
            success = (cursor.rowcount == 1)
        except (Exception, psycopg2.Error) as error:
            traceback.print_exc()
        finally:
            if connection:
                cursor.close()
                connection.close()
        return success
    def list(self):
        results = []
        try:
            connection = psycopg2.connect(user=self._usr, password=self._psw, port=self._port, database=self._db)
            cursor = connection.cursor()
            cursor.execute("SELECT cpf, name, contact FROM artesao")
            registers = cursor.fetchall()
            for r in registers:
                a = Artisan()
                a.cpf = r[0]
                a.name = r[1]
                a.contact = r[2]
                results.append(a)
        except (Exception, psycopg2.Error) as error:
            traceback.print_exc()
        finally:
            if connection:
                cursor.close()
                connection.close()
        return results