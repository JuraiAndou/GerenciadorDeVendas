import credentials
import psycopg2
import traceback

from types import TracebackType

class ArtDAO(object):
    def __init__(self):
        pass
    def insert(self, cpf, name, contact):
        success = False
        try:
            connection = psycopg2.connect(user=credentials.pg_user, password=credentials.pg_password, port=credentials.pg_port, database=credentials.pg_database)
            cursor = connection.cursor()
            cursor.execute("INSERT INTO artesao VALUES (" + cpf + ", \'" + name + "\', \'" + contact + "\', " + ")")
            connection.commit()
            success = (cursor.rowcount == 1)
        except (Exception, psycopg2.Error) as error:
            traceback.print_exc()
        finally:
            if connection:
                cursor.close()
        return success