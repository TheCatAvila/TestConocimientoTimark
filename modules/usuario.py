class Usuario():

    def __init__(self, mysql):
        self.mysql = mysql

    def RegistrarUsuario(self, nombre, email, contrasena):

        if len(email) < 1:
            return "Error, el email no contiene nada."
        
        if '@' not in email or '.' not in email:
            return "Error, email inválido."
        
        try:
            with self.mysql.connection.cursor() as cursor:

                query = """
                    INSERT INTO usuarios (
                        nombre, 
                        email, 
                        contrasena
                    )
                    VALUES (%s, %s, %s)"""
                
                cursor.execute(query, (nombre, email, contrasena))
                self.mysql.connection.commit()

                return True

        except Exception as e:
            return print(f"Error al registrar el usuario: {e}")