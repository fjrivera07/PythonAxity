import json


def cargar_usuarios(ruta_archivo):
    try:
        with open(ruta_archivo, "r", encoding="utf-8") as archivo:
            return json.load(archivo)

    except FileNotFoundError:
        print("El archivo no existe")
        return []

    except json.JSONDecodeError:
        print("JSON inválido")
        return []


def filtrar_usuarios_activos(usuarios):
    return [u for u in usuarios if u["activo"]]


def mostrar_usuarios(usuarios):
    for usuario in usuarios:
        match usuario["activo"]:
            case True:
                estado = "Activo"
            case False:
                estado = "Inactivo"

        print(f'{usuario["nombre"]} - {estado}')


usuarios = cargar_usuarios("usuarios.json")

usuarios_activos = filtrar_usuarios_activos(usuarios)

mostrar_usuarios(usuarios_activos)
