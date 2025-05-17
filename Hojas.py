import json
import os
from datetime import datetime
from colorama import Fore, Style, init
from fpdf import FPDF
import re

init(autoreset=True)

BASE_DIR = "BaseDeDatos"
if not os.path.exists(BASE_DIR):
    os.makedirs(BASE_DIR)

def guardar_json_pdf(cedula, datos):
    ruta_carpeta = os.path.join(BASE_DIR, str(cedula))
    if not os.path.exists(ruta_carpeta):
        os.makedirs(ruta_carpeta)

    # Guardar JSON
    ruta_json = os.path.join(ruta_carpeta, "hoja_de_vida.json")
    with open(ruta_json, "w", encoding="utf-8") as f:
        json.dump(datos, f, indent=4, default=str)

    # Generar PDF
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=12)

    pdf.cell(0, 10, "HOJA DE VIDA", ln=True, align='C')
    pdf.cell(0, 10, f"Cédula: {cedula}", ln=True)
    for campo, valor in datos.items():
        if campo in ["formaciones", "experiencias", "habilidades", "referencias"]:
            pdf.cell(0, 10, f"{campo.capitalize()}:", ln=True)
            if isinstance(valor, list):
                for item in valor:
                    for clave, contenido in item.items():
                        pdf.cell(0, 10, f"  {clave}: {contenido}", ln=True)
            elif isinstance(valor, dict):
                for clave, contenido in valor.items():
                    pdf.cell(0, 10, f"  {clave}:", ln=True)
                    for sub_clave, sub_valor in contenido.items():
                        pdf.cell(0, 10, f"    {sub_clave}: {sub_valor}", ln=True)
            else:
                pdf.cell(0, 10, f"  {valor}", ln=True)
        else:
            pdf.cell(0, 10, f"{campo.capitalize()}: {valor}", ln=True)

    pdf.output(os.path.join(ruta_carpeta, "hoja_de_vida.pdf"))

def cargar_base():
    base = {}
    for carpeta in os.listdir(BASE_DIR):
        ruta = os.path.join(BASE_DIR, carpeta, "hoja_de_vida.json")
        if os.path.exists(ruta):
            with open(ruta, encoding="utf-8") as f:
                base[int(carpeta)] = json.load(f)
    return base

def crear_hoja_de_vida():
    hoja = {}

    while True:
        nombre = input("Nombre completo: ")
        if all(char.isalpha() or char.isspace() for char in nombre):
            break
        print("Nombre inválido.")

    while True:
        try:
            cedula = int(input("Cédula: "))
            break
        except:
            print("Cédula inválida.")

    while True:
        try:
            contacto = int(input("Número de contacto: "))
            break
        except:
            print("Contacto inválido.")

    direccion = input("Dirección de residencia: ")

    while True:
        correo = input("Correo electrónico: ")
        if re.match(r"^[\w\.-]+@[\w\.-]+\.\w+$", correo):
            break
        print("Correo inválido.")

    while True:
        fecha = input("Fecha de nacimiento (dd/mm/yyyy): ")
        try:
            fecha_nac = datetime.strptime(fecha, "%d/%m/%Y")
            break
        except:
            print("Fecha inválida.")

    formaciones, experiencias = [], []
    referencias, habilidades = {}, []

    if input("¿Tiene formación académica? (si/no): ").lower() == "si":
        while True:
            formacion = input("Formación: ")
            institucion = input("Institución: ")
            titulo = input("Título: ")
            año = input("Año de finalización: ")
            formaciones.append({
                "Formación": formacion,
                "Institución": institucion,
                "Título": titulo,
                "Año": año
            })
            if input("¿Agregar otra formación? (si/no): ") == "no":
                break

    if input("¿Tiene experiencia laboral? (si/no): ").lower() == "si":
        while True:
            empresa = input("Empresa: ")
            cargo = input("Cargo: ")
            funcion = input("Función: ")
            duracion = input("Duración: ")
            experiencias.append({
                "Empresa": empresa,
                "Cargo": cargo,
                "Función": funcion,
                "Duración": duracion
            })
            if input("¿Agregar otra experiencia? (si/no): ") == "no":
                break

    if input("¿Tiene referencias? (si/no): ").lower() == "si":
        while True:
            ref = input("Nombre de la persona o empresa: ")
            rel = input("Relación: ")
            tel = input("Teléfono: ")
            referencias[ref] = {"Relación": rel, "Teléfono": tel}
            if input("¿Agregar otra referencia? (si/no): ") == "no":
                break

    while True:
        habilidad = input("Habilidad: ")
        habilidades.append(habilidad)
        if input("¿Agregar otra habilidad? (si/no): ") == "no":
            break

    hoja["nombre"] = nombre
    hoja["contacto"] = contacto
    hoja["direccion"] = direccion
    hoja["correo"] = correo
    hoja["fecha nacimiento"] = fecha_nac.strftime("%d/%m/%Y")
    hoja["formaciones"] = formaciones
    hoja["experiencias"] = experiencias
    hoja["referencias"] = referencias
    hoja["habilidades"] = habilidades

    guardar_json_pdf(cedula, hoja)
    print(Fore.GREEN + "Hoja de vida guardada correctamente." + Style.RESET_ALL)

def buscar_hoja_de_vida():
    base = cargar_base()
    if not base:
        print("No hay hojas de vida registradas.")
        return

    while True:
        op = input("\nBuscar por: 1. Nombre 2. Cédula 3. Correo: ")
        if op == "1":
            nombre = input("Ingrese el nombre completo: ")
            for datos in base.values():
                if datos["nombre"].lower() == nombre.lower():
                    print(json.dumps(datos, indent=4, ensure_ascii=False))
        elif op == "2":
            cedula = int(input("Ingrese su cédula: "))
            if cedula in base:
                print(json.dumps(base[cedula], indent=4, ensure_ascii=False))
        elif op == "3":
            correo = input("Ingrese su correo: ")
            for datos in base.values():
                if datos["correo"].lower() == correo.lower():
                    print(json.dumps(datos, indent=4, ensure_ascii=False))

        if input("¿Desea hacer otra búsqueda? (si/no): ").lower() != "si":
            break

def modificar_hoja_de_vida():
    base = cargar_base()
    try:
        cedula = int(input("Ingrese la cédula a modificar: "))
        if cedula not in base:
            print("No existe esa cédula.")
            return

        hoja = base[cedula]
        print("Campos disponibles: nombre, contacto, direccion, correo, fecha nacimiento, habilidades")
        campo = input("¿Qué campo desea modificar?: ").lower()

        if campo == "nombre":
            hoja["nombre"] = input("Nuevo nombre: ")
        elif campo == "contacto":
            hoja["contacto"] = int(input("Nuevo contacto: "))
        elif campo == "direccion":
            hoja["direccion"] = input("Nueva dirección: ")
        elif campo == "correo":
            hoja["correo"] = input("Nuevo correo: ")
        elif campo == "fecha nacimiento":
            nueva_fecha = input("Nueva fecha (dd/mm/yyyy): ")
            hoja["fecha nacimiento"] = datetime.strptime(nueva_fecha, "%d/%m/%Y").strftime("%d/%m/%Y")
        elif campo == "habilidades":
            hoja["habilidades"] = []
            while True:
                hab = input("Nueva habilidad: ")
                hoja["habilidades"].append(hab)
                if input("¿Agregar otra? (si/no): ") == "no":
                    break
        else:
            print("Campo inválido.")

        guardar_json_pdf(cedula, hoja)
        print("Hoja de vida modificada.")

    except ValueError:
        print("Error de entrada.")

# Menú principal
def menu():
    while True:
        print("\n" + "---"*10)
        print("1. Crear hoja de vida")
        print("2. Buscar hoja de vida")
        print("3. Modificar hoja de vida")
        print("4. Salir")
        op = input("Seleccione una opción: ")

        if op == "1":
            crear_hoja_de_vida()
        elif op == "2":
            buscar_hoja_de_vida()
        elif op == "3":
            modificar_hoja_de_vida()
        elif op == "4":
            break
        else:
            print("Opción inválida.")

menu()