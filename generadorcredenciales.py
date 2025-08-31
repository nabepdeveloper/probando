import random
import string
import pandas as pd

def generar_contraseña(longitud=10):
    caracteres = string.ascii_letters + string.digits + "!@#$%^&*()-_=+"
    return ''.join(random.choice(caracteres) for _ in range(longitud))

usuarios = []

for i in range(1, 201):
    usuarios.append(f"op_numero{i}")

for i in range(1, 11):
    usuarios.append(f"sup_numero{i}")

for i in range(1, 6):
    usuarios.append(f"adm_numero{i}")

datos = []
for usuario in usuarios:
    contraseña = generar_contraseña()
    datos.append([usuario, contraseña])

df = pd.DataFrame(datos, columns=["usuario", "contraseña"])

df.to_excel("usuarios_generados.xlsx", index=False)
print("✅ Archivo 'usuarios_generados.xlsx' creado con 215 usuarios y contraseñas seguras.")