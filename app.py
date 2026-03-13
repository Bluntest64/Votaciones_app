from flask import Flask, render_template, request
import config
import os

app = Flask(__name__)


@app.route("/")
def inicio():
    return render_template("index.html")


@app.route("/registro")
def registro():
    return render_template("registro.html")


@app.route("/consulta")
def consulta():
    return render_template("consulta.html")


@app.route("/datos", methods=["POST"])
def datos():

    conexion = config.crear_conexion()
    cursor = conexion.cursor()

    documento = request.form["documento"]
    nombre = request.form["nombre"]
    ciudad = request.form["ciudad"]
    telefono = request.form["telefono"]

    sql = """
    INSERT INTO ciudadanos (documento, nombre, ciudad, telefono)
    VALUES (%s, %s, %s, %s)
    """

    valores = (documento, nombre, ciudad, telefono)

    cursor.execute(sql, valores)
    conexion.commit()

    cursor.close()
    conexion.close()

    return render_template("index.html")


@app.route("/resultado", methods=["POST"])
def resultado():

    conexion = config.crear_conexion()
    cursor = conexion.cursor()

    documento = request.form["documento"]

    sql = "SELECT lugar, direccion, mesa FROM puestos_votacion WHERE documento = %s"

    cursor.execute(sql, (documento,))
    datos = cursor.fetchone()

    if datos:
        lugar = datos[0]
        direccion = datos[1]
        mesa = datos[2]
    else:
        lugar = "No encontrado"
        direccion = "-"
        mesa = "-"

    cursor.close()
    conexion.close()

    return render_template(
        "resultado.html",
        documento=documento,
        lugar=lugar,
        direccion=direccion,
        mesa=mesa
    )


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))