from datetime import datetime
from colorama import Fore,Style, init
init(autoreset=True)
import re

hoja_de_vida = {}
formaciones_aca = {}
formaciones = []
diccionario_experiencia = {}
experiencias = []
referencias = {}
lista_habilidades = []

print("---"*30)
print("VITAECONSOLE")
print("---"*30)

def Crear_Hoja_De_Vida():
    Activacion = True
    while Activacion:
        aName = True
        while aName:
            nombre = input("Ingrese su nombre completo: ")
            if all(char.isalpha() or char == ' ' for char in nombre):
                aName = False
            else:
                print("Ingrese solo letras y espacios.")

        aID = True
        while aID:
            try: 
                num_id = int(input("Ingrese el numero de su documento de identidad: \n"))
                aID = False
            except ValueError:
                print("Ingresa solamente números en el documento.")

        aContact = True
        while aContact:
            try:
                contacto = int(input("Ingrese el numero de contacto: \n"))
                aContact = False
            except:
                print("Ingrese un número válido.")

        direccion = input("Ingrese la direccion de residencia \n")

        aMail = True
        while aMail:
            correo = input("Ingrese su correo electronico: \n")
            if re.match(r"^[\w\.-]+@[\w\.-]+\.\w+$", correo):
                aMail = False
            else:
                print("Ingrese una dirección de correo válida.")

        aBorn = True
        while aBorn:
            FDN = input("Ingrese su fecha de nacimiento (dd/mm/aaaa): ")
            try:
                fecha_nacimiento = datetime.strptime(FDN, "%d/%m/%Y")
                if fecha_nacimiento > datetime.now():
                    print("La fecha no puede estar en el futuro.")
                else:
                    aBorn = False
            except ValueError:
                print("Formato incorrecto o fecha inválida. Use el formato dd/mm/aaaa.")

        pregunt_formacion_academica = input("Tiene formacion academica? (si/no)")

        if pregunt_formacion_academica == "si": 
            mas_formaciones_academic = True
            while mas_formaciones_academic:
                formacion_academica = input("Ingrese su formacion academica: \n")
                institucion_academ = input("Ingrese el nombre de la institucion en la que hizo esta formacion: \n ")
                titulo = input("Ingrese el titulo otorgado de esta formacion: \n")
                anios_academicos = input("Ingrese en que año terminó esta formacion:  \n")
                mas_formaciones = input("Tiene mas formaciones? (si/no) \n")

                formaciones_aca[formacion_academica] = {
                    "formacion" : formacion_academica,
                    "institucion" : institucion_academ,
                    "titulo" : titulo,
                    "años" : anios_academicos
                }

                if mas_formaciones == "si":
                    print("")
                elif mas_formaciones == "no":
                    formaciones.append(formaciones_aca)
                    mas_formaciones_academic = False

        elif pregunt_formacion_academica == "no":
            print("no tiene formacion academica")

        ingresar_mas_experiencia = True
        while ingresar_mas_experiencia:
            exp_profesional  = input("Tiene experiencia en el ambito laboral? (si/no)\n")
            if exp_profesional == "si":
                experiencia = input("Ingrese su experiencia: \n ")
                empresas = input("Ingrese en que empresa adquirió la experiencia:  \n")
                cargo = input("Ingrese el cargo que tenía en esta empresa \n ") 
                funcion = input("Ingrese la funcion que cumplia en esta empresa: \n")
                duracion = input("Ingrese cuanto tiempo duró en la formacion: ")
                diccionario_experiencia[experiencia] = {
                    "empresa" : empresas,
                    "cargo" : cargo,
                    "funcion" : funcion,
                    "duracion" : duracion,
                }

                agregar_mas_exp = input("Desea agregar mas experiencia? (si/no) \n")
                if agregar_mas_exp == "si":
                    print("")
                elif agregar_mas_exp == "no":
                    experiencias.append(diccionario_experiencia)
                    ingresar_mas_experiencia = False
            elif exp_profesional == "no":
                print("no")
                ingresar_mas_experiencia = False

        referencias_pregunta = input("Tiene referencias laborales o personales? (si/no) \n")
        if referencias_pregunta == "si":
            agg_referencia = True
            while agg_referencia:
                referencia = input("Ingrese el nombre de la empresa o persona que lo referencia: \n")
                relacion_persona = input("Ingrese que relacion tiene con la persona: \n")
                telefono_r = int(input("Ingrese el numero telefonico de la persona que lo referencia: \n"))

                referencias[referencia] = {
                    "relacion" : relacion_persona,
                    "contacto": telefono_r
                }

                agregar_referencia = input("Desea agregar otra referencia? (si/no) \n")
                if agregar_referencia == "si":
                    print("")
                elif agregar_referencia == "no":
                    agg_referencia = False
        elif referencias_pregunta == "no":
            print("No tiene referencias \n")

        agrega_mas_habilidades = True
        while agrega_mas_habilidades:
            habilidad = input("Ingrese sus habilidades: \n")
            mas_habilidades = input("Tiene mas habilidades: (si/no)")
            lista_habilidades.append(habilidad)
            if mas_habilidades == "si":
                print("")
            elif mas_habilidades == "no":
                agrega_mas_habilidades = False

        hoja_de_vida[num_id] = {
            "nombre" : nombre,
            "contacto" : contacto,
            "direccion": direccion,
            "correo" : correo,
            "fecha nacimiento": fecha_nacimiento,
            "formaciones" : formaciones,
            "experiencias" : experiencias,
            "referencias" : referencias,
            "habilidades" : lista_habilidades
        }

        print("\n" + "---" * 30)
        print("HOJA DE VIDA GENERADA")
        print("---" * 30 + "\n")

        for cedula, datos in hoja_de_vida.items():
            print(f"Cédula: {cedula}")
            print(f"Nombre: {datos['nombre']}")
            print(f"Contacto: {datos['contacto']}")
            print(f"Dirección: {datos['direccion']}")
            print(f"Correo: {datos['correo']}")
            print(f"Fecha de nacimiento: {datos['fecha nacimiento']}")

            print("\nFormaciones:")
            if datos["formaciones"]:
                for formacion in datos["formaciones"]:
                    for clave, valor in formacion.items():
                        print(f" - {clave}: {valor}")
            else:
                print("No registra formaciones académicas.")

            print("\nExperiencias:")
            if datos["experiencias"]:
                for experiencia in datos["experiencias"]:
                    for clave, valor in experiencia.items():
                        print(f" - {clave}: {valor}")
            else:
                print("No registra experiencia laboral.")

            print("\nReferencias:")
            if datos["referencias"]:
                for referencia, info in datos["referencias"].items():
                    print(f" - {referencia}:")
                    for clave, valor in info.items():
                        print(f"    {clave}: {valor}")
            else:
                print("No registra referencias.")

            print("\nHabilidades:")
            if datos["habilidades"]:
                for habilidad in datos["habilidades"]:
                    print(f" - {habilidad}")
            else:
                print("No registra habilidades.")

def Modificar_Hoja_De_Vida():
    try:
        cedula = int(input("Ingrese la cédula del registro que desea modificar: "))
        if cedula in hoja_de_vida:
            persona = hoja_de_vida[cedula]
            print("¿Qué desea modificar? (nombre/contacto/direccion/correo/fecha/formaciones/experiencias/referencias/habilidades)")
            campo = input("Campo a modificar: ").lower()

            if campo in ["nombre", "contacto", "direccion", "correo", "fecha"]:
                nuevo_valor = input("Ingrese el nuevo valor: ")
                if campo == "contacto":
                    nuevo_valor = int(nuevo_valor)
                elif campo == "fecha":
                    nuevo_valor = datetime.strptime(nuevo_valor, "%d/%m/%Y")
                    campo = "fecha nacimiento"
                persona[campo] = nuevo_valor

            elif campo == "habilidades":
                persona["habilidades"].clear()
                print("Ingrese nuevamente las habilidades:")
                while True:
                    habilidad = input("Habilidad: ")
                    persona["habilidades"].append(habilidad)
                    if input("¿Agregar más habilidades? (si/no): ") == "no":
                        break

            print("Modificación realizada con éxito.\n")
        else:
            print("No se encontró una hoja de vida con esa cédula.")
    except ValueError:
        print("Cédula inválida.")

Crear_Hoja_De_Vida()
