from flask import Flask, render_template, request, redirect, url_for
import pandas as pd
from datetime import datetime

app = Flask(__name__)

def registrar_log(mensaje):
    with open("log.txt", "a", encoding="utf-8") as f:
        f.write(f"[{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}] {mensaje}\n")

@app.route('/', methods=['GET', 'POST'])
def login():
    mensaje = ""
    if request.method == 'POST':
        usuario = request.form['usuario']
        contraseña = request.form['contraseña']

        try:
            df = pd.read_excel('usuarios.xlsx')

            if usuario not in df['usuario'].values:
                mensaje = "❌ Usuario no existe."
                registrar_log(f"Intento con usuario inexistente: '{usuario}'")
            else:
                fila = df[df['usuario'] == usuario]
                contraseña_real = fila.iloc[0]['contraseña']
                if contraseña == contraseña_real:
                    nombre = fila.iloc[0]['nombre']
                    apellido = fila.iloc[0]['apellido']
                    registrar_log(f"Inicio de sesión exitoso: '{usuario}'")
                    return redirect(url_for('panel', usuario=usuario, nombre=nombre, apellido=apellido))
                else:
                    mensaje = "❌ Contraseña incorrecta."
                    registrar_log(f"Contraseña incorrecta para usuario '{usuario}': intentó '{contraseña}' | contraseña real: '{contraseña_real}'")

        except Exception as e:
            mensaje = f"⚠️ Error al validar: {e}"
            registrar_log(f"Error al validar usuario '{usuario}': {e}")

    return render_template('login.html', mensaje=mensaje)

@app.route('/panel')
def panel():
    usuario = request.args.get('usuario', 'usuario')
    nombre = request.args.get('nombre', '')
    apellido = request.args.get('apellido', '')
    return render_template('panel.html', usuario=usuario, nombre=nombre, apellido=apellido)

@app.route('/test')
def test():
    return "Servidor activo ✅"

if __name__ == '__main__':
    import os

port = int(os.environ.get("PORT", 5000))
app.run(host="0.0.0.0", port=port, debug=True)