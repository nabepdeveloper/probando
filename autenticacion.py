import pandas as pd

def validar_login(usuario_input, contraseña_input):
    try:
        df = pd.read_excel('usuarios.xlsx', sheet_name='Credenciales')

        usuario_valido = df[
            (df['usuario'] == usuario_input) & 
            (df['contraseña'] == contraseña_input)
        ]

        if not usuario_valido.empty:
            print(f"✅ Acceso concedido. Bienvenido, {usuario_input}")
            return True
        else:
            print("❌ Usuario o contraseña incorrectos.")
            return False

    except FileNotFoundError:
        print("⚠️ Archivo Excel no encontrado.")
        return False
    except Exception as e:
        print(f"⚠️ Error al validar: {e}")
        return False

usuario = input("Usuario: ")
contraseña = input("Contraseña: ")

validar_login(usuario, contraseña)