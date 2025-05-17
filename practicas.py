import re
from datetime import datetime
from colorama import Fore, Style, init
import os
from EXPORTAR import exportar_hoja_txt()

init(autoreset=True)

hoja_de_vida = {}

def validar_nombre():
    while True:
        nombre = input("Ingrese su nombre completo: ")
        if all(char.isalpha() or char == ' ' for char in nombre) and nombre.strip() != "":
            return nombre
        else:
            print("Ingrese solo letras y espacios.")

def validar_documento():
    while True:
        try:
            num_id = int(input("Ingrese el número de su documento de identidad: "))
            return num_id
        except ValueError:
            print("Ingrese solo números en el documento.")

def validar_contacto():
    while True:
        try:
            contacto = int(input("Ingrese el número de contacto: "))
            return contacto
        except ValueError:
            print("Ingrese un número válido.")

def validar_correo():
    while True:
        correo = input("Ingrese su correo electrónico: ")
        if re.match(r"^[\w\.-]+@[\w\.-]+\.\w+$", correo):
            return correo
        else:
            print("Ingrese una dirección de correo válida.")

def validar_fecha_nacimiento():
    while True:
        FDN = input("Ingrese su fecha de nacimiento (dd/mm/aaaa): ")
        try:
            fecha = datetime.strptime(FDN, "%d/%m/%Y")
            if fecha > datetime.now():
                print("La fecha no puede estar en el futuro.")
            else:
                return fecha
        except ValueError:
            print("Formato incorrecto o fecha inválida. Use dd/mm/aaaa.")

def guardar_txt(cedula):
    if not os.path.exists("Hojas_de_Vida"):
        os.mkdir("Hojas_de_Vida")
    archivo = f"Hojas_de_Vida/HDV_{cedula}.txt"
    with open(archivo, "w", encoding="utf-8") as f:
        datos = hoja_de_vida[cedula]
        f.write(f"Cédula: {cedula}\n")
        f.write(f"Nombre: {datos['nombre']}\n")
        f.write(f"Contacto: {datos['contacto']}\n")
        f.write(f"Dirección: {datos['direccion']}\n")
        f.write(f"Correo: {datos['correo']}\n")
        f.write(f"Fecha de nacimiento: {datos['fecha nacimiento'].strftime('%d/%m/%Y')}\n\n")
        f.write("Formaciones:\n")
        if datos["formaciones"]:
            for form in datos["formaciones"]:
                for clave, valor in form.items():
                    f.write(f" - {clave}: {valor}\n")
        else:
            f.write("No registra formaciones académicas.\n")
        f.write("\nExperiencias:\n")
        if datos["experiencias"]:
            for exp in datos["experiencias"]:
                for clave, valor in exp.items():
                    f.write(f" - {clave}: {valor}\n")
        else:
            f.write("No registra experiencia laboral.\n")
        f.write("\nReferencias:\n")
        if datos["referencias"]:
            for ref, info in datos["referencias"].items():
                f.write(f" - {ref}:\n")
                for clave, valor in info.items():
                    f.write(f"    {clave}: {valor}\n")
        else:
            f.write("No registra referencias.\n")
        f.write("\nHabilidades:\n")
        if datos["habilidades"]:
            for hab in datos["habilidades"]:
                f.write(f" - {hab}\n")
        else:
            f.write("No registra habilidades.\n")

def Crear_Hoja_De_Vida():
    nombre = validar_nombre()
    num_id = validar_documento()
    contacto = validar_contacto()
    direccion = input("Ingrese la direccion de residencia: ")
    correo = validar_correo()
    fecha_nacimiento = validar_fecha_nacimiento()

    formaciones_aca = {}
    formaciones = []
    preguntar_formacion_academica = input("Tiene formación académica? (si/no): ").lower()
    if preguntar_formacion_academica == "si":
        while True:
            formacion_academica = input("Ingrese su formación académica: ")
            institucion_academ = input("Ingrese el nombre de la institución: ")
            titulo = input("Ingrese el título otorgado: ")
            anios_academicos = input("Ingrese en qué año terminó esta formación: ")
            formaciones_aca = {
                "formacion": formacion_academica,
                "institucion": institucion_academ,
                "titulo": titulo,
                "años": anios_academicos
            }
            formaciones.append(formaciones_aca)
            mas = input("¿Tiene más formaciones? (si/no): ").lower()
            if mas != "si":
                break
    else:
        print("No tiene formación académica")

    diccionario_experiencia = {}
    experiencias = []
    exp_profesional = input("Tiene experiencia laboral? (si/no): ").lower()
    if exp_profesional == "si":
        while True:
            experiencia = input("Ingrese su experiencia: ")
            empresa = input("Ingrese la empresa donde trabajó: ")
            cargo = input("Ingrese el cargo que tenía: ")
            funcion = input("Ingrese la función que cumplía: ")
            duracion = input("Ingrese la duración: ")
            diccionario_experiencia = {
                "experiencia": experiencia,
                "empresa": empresa,
                "cargo": cargo,
                "funcion": funcion,
                "duracion": duracion
            }
            experiencias.append(diccionario_experiencia)
            mas_exp = input("¿Desea agregar más experiencia? (si/no): ").lower()
            if mas_exp != "si":
                break
    else:
        print("No tiene experiencia laboral")

    referencias = {}
    referencias_pregunta = input("Tiene referencias laborales o personales? (si/no): ").lower()
    if referencias_pregunta == "si":
        while True:
            referencia = input("Ingrese nombre de la persona o empresa que referencia: ")
            relacion_persona = input("Ingrese la relación: ")
            while True:
                try:
                    telefono_r = int(input("Ingrese teléfono de la referencia: "))
                    break
                except ValueError:
                    print("Ingrese un número válido.")
            referencias[referencia] = {
                "relacion": relacion_persona,
                "contacto": telefono_r
            }
            mas_ref = input("¿Desea agregar otra referencia? (si/no): ").lower()
            if mas_ref != "si":
                break
    else:
        print("No tiene referencias")

    lista_habilidades = []
    while True:
        habilidad = input("Ingrese una habilidad: ")
        lista_habilidades.append(habilidad)
        mas_hab = input("¿Tiene más habilidades? (si/no): ").lower()
        if mas_hab != "si":
            break

    hoja_de_vida[num_id] = {
        "nombre": nombre,
        "contacto": contacto,
        "direccion": direccion,
        "correo": correo,
        "fecha nacimiento": fecha_nacimiento,
        "formaciones": formaciones,
        "experiencias": experiencias,
        "referencias": referencias,
        "habilidades": lista_habilidades
    }

    print("\n---" * 10)
    print("HOJA DE VIDA GENERADA")
    print("---" * 10 + "\n")

    guardar_txt(num_id)

def Buscar_HDV():
    if not hoja_de_vida:
        print("No hay hojas de vida registradas.")
        return
    while True:
        print(f"\n{Fore.BLUE}Consulta una hoja de vida{Style.RESET_ALL}\n")
        consulta = input(f"¿Cómo desea consultar su hoja de vida? {Fore.GREEN}1.{Style.RESET_ALL} Nombre. {Fore.GREEN}2.{Style.RESET_ALL} Documento. {Fore.GREEN}3.{Style.RESET_ALL} Correo electrónico. ")
        encontrado = False
        if consulta == '1':
            nombre = input("Ingrese el nombre completo (sin tildes ni puntos): ")
            for cedula, datos in hoja_de_vida.items():
                if datos["nombre"].lower() == nombre.lower():
                    imprimir_hoja(cedula, datos)
                    encontrado = True
        elif consulta == '2':
            try:
                documento = int(input("Ingrese su documento: "))
            except ValueError:
                print("Documento inválido.")
                continue
            if documento in hoja_de_vida:
                imprimir_hoja(documento, hoja_de_vida[documento])
                encontrado = True
        elif consulta == '3':
            correo = input("Ingrese su correo electrónico: ")
            for cedula, datos in hoja_de_vida.items():
                if datos["correo"].lower() == correo.lower():
                    imprimir_hoja(cedula, datos)
                    encontrado = True
        else:
            print("Opción inválida.")
            continue

        if not encontrado:
            print("No se encontró la hoja de vida.")

        otra = input("¿Desea buscar otra hoja de vida? 1. Sí. Cualquier otra tecla para salir: ")
        if otra != '1':
            break

def imprimir_hoja(cedula, datos):
    print(f"Cédula: {cedula}")
    print(f"Nombre: {datos['nombre']}")
    print(f"Contacto: {datos['contacto']}")
    print(f"Dirección: {datos['direccion']}")
    print(f"Correo: {datos['correo']}")
    print(f"Fecha de nacimiento: {datos['fecha nacimiento'].strftime('%d/%m/%Y')}\n")
    print("Formaciones:")
    if datos["formaciones"]:
        for form in datos["formaciones"]:
            for clave, valor in form.items():
                print(f" - {clave}: {valor}")
    else:
        print("No registra formaciones académicas.")
    print("\nExperiencias:")
    if datos["experiencias"]:
        for exp in datos["experiencias"]:
            for clave, valor in exp.items():
                print(f" - {clave}: {valor}")
    else:
        print("No registra experiencia laboral.")
    print("\nReferencias:")
    if datos["referencias"]:
        for ref, info in datos["referencias"].items():
            print(f" - {ref}:")
            for clave, valor in info.items():
                print(f"    {clave}: {valor}")
    else:
        print("No registra referencias.")
    print("\nHabilidades:")
    if datos["habilidades"]:
        for hab in datos["habilidades"]:
            print(f" - {hab}")
    else:
        print("No registra habilidades.")

def Modificar_HDV():
    if not hoja_de_vida:
        print("No hay hojas de vida registradas para modificar.")
        return
    while True:
        try:
            documento = int(input("Ingrese el número de documento de la hoja de vida a modificar: "))
        except ValueError:
            print("Documento inválido.")
            continue
        if documento not in hoja_de_vida:
            print("No se encontró esa hoja de vida.")
            continue
        datos = hoja_de_vida[documento]
        print(f"Modificando hoja de vida de {datos['nombre']} (Documento: {documento})")
        while True:
            print("\n¿Qué desea modificar?")
            print("1. Nombre")
            print("2. Contacto")
            print("3. Dirección")
            print("4. Correo")
            print("5. Fecha de nacimiento")
            print("6. Formaciones académicas")
            print("7. Experiencias laborales")
            print("8. Referencias")
            print("9. Habilidades")
            print("10. Guardar y salir")
            opcion = input("Ingrese una opción: ")
            if opcion == "1":
                datos["nombre"] = validar_nombre()
            elif opcion == "2":
                datos["contacto"] = validar_contacto()
            elif opcion == "3":
                datos["direccion"] = input("Ingrese nueva dirección: ")
            elif opcion == "4":
                datos["correo"] = validar_correo()
            elif opcion == "5":
                datos["fecha nacimiento"] = validar_fecha_nacimiento()
            elif opcion == "6":
                datos["formaciones"] = []
                print("Ingrese las nuevas formaciones académicas:")
                while True:
                    formacion_academica = input("Ingrese su formación académica (o deje vacío para terminar): ")
                    if formacion_academica == "":
                        break
                    institucion_academ = input("Ingrese el nombre de la institución: ")
                    titulo = input("Ingrese el título otorgado: ")
                    anios_academicos = input("Ingrese en qué año terminó esta formación: ")
                    formacion = {
                        "formacion": formacion_academica,
                        "institucion": institucion_academ,
                        "titulo": titulo,
                        "años": anios_academicos
                    }
                    datos["formaciones"].append(formacion)
            elif opcion == "7":
                datos["experiencias"] = []
                print("Ingrese las nuevas experiencias laborales:")
                while True:
                    experiencia = input("Ingrese su experiencia (o deje vacío para terminar): ")
                    if experiencia == "":
                        break
                    empresa = input("Ingrese la empresa donde trabajó: ")
                    cargo = input("Ingrese el cargo que tenía: ")
                    funcion = input("Ingrese la función que cumplía: ")
                    duracion = input("Ingrese la duración: ")
                    experiencia_dict = {
                        "experiencia": experiencia,
                        "empresa": empresa,
                        "cargo": cargo,
                        "funcion": funcion,
                        "duracion": duracion
                    }
                    datos["experiencias"].append(experiencia_dict)
            elif opcion == "8":
                datos["referencias"] = {}
                print("Ingrese las nuevas referencias:")
                while True:
                    referencia = input("Ingrese nombre de la persona o empresa que referencia (o deje vacío para terminar): ")
                    if referencia == "":
                        break
                    relacion_persona = input("Ingrese la relación: ")
                    while True:
                        try:
                            telefono_r = int(input("Ingrese teléfono de la referencia: "))
                            break
                        except ValueError:
                            print("Ingrese un número válido.")
                    datos["referencias"][referencia] = {
                        "relacion": relacion_persona,
                        "contacto": telefono_r
                    }
            elif opcion == "9":
                datos["habilidades"] = []
                print("Ingrese las nuevas habilidades:")
                while True:
                    habilidad = input("Ingrese una habilidad (o deje vacío para terminar): ")
                    if habilidad == "":
                        break
                    datos["habilidades"].append(habilidad)
            elif opcion == "10":
                hoja_de_vida[documento] = datos
                guardar_txt(documento)
                print("Cambios guardados.")
                break
            else:
                print("Opción inválida.")

        break

def menu():
    while True:
        print("\n" + "---" * 10)
        print("Menú de hoja de vida")
        print("1. Crear hoja de vida")
        print("2. Buscar hoja de vida")
        print("3. Modificar hoja de vida")
        print("4. Exportar Hoja de Vida")
        print("5. Salir")
        opcion = input("Ingrese una opción: ")
        if opcion == "1":
            Crear_Hoja_De_Vida()
        elif opcion == "2":
            Buscar_HDV()
        elif opcion == "3":
            Modificar_HDV()
        elif opcion == "4":
            exportar_hoja_txt()
        elif opcion == "5":
            break 
        else:
            print("Opción inválida.")

if __name__ == "__main__":
    menu()
