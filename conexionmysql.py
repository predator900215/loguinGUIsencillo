import mysql.connector


class Connection:
    def __init__(self):
        self.connection = mysql.connector.connect(
            host='',
            port='',
            user='',
            password='',
            database=''

        )

    def inserta_usuario(self, usuario, contrasenia):
        cursor = self.connection.cursor()
        action = "INSERT INTO registro (usuario, contrasenia) VALUES (%s, %s)"
        cursor.execute(action, (usuario, contrasenia))
        self.connection.commit()
        cursor.close()

    def consulta_usuario(self, usuario, contrasenia):
        cursor = self.connection.cursor()
        action = "SELECT * FROM registro WHERE usuario = %s AND contrasenia = %s"
        cursor.execute(action, (usuario, contrasenia))
        resultados = cursor.fetchall()
        self.connection.commit()
        cursor.close()
        return resultados

    def borrar_usuario(self, usuario, contrasenia):
        cursor = self.connection.cursor()
        action = "DELETE FROM registro WHERE usuario = %s AND contrasenia = %s"
        cursor.execute(action, (usuario, contrasenia))
        self.connection.commit()
        cursor.close()
