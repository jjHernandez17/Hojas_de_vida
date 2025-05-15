from operator import truediv


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

nombre = input("Ingrese su nombre completo: \n")
num_id = int(input("Ingrese el numero de su documenoto de identidad: \n"))
contacto = int(input("Ingrese el numero de contacto: \n"))
direccion = input("Ingrese la direccion de residencia \n")
correo = input("Ingrese su correo electronico: \n")
fecha_nacimiento = input("Ingrese su fecha de nacimiento: \n")


pregunt_formacion_academica = input("Tiene formacion academica? (si/no)")

if pregunt_formacion_academica == "si": 
    mas_formaciones_academic = True
    while mas_formaciones_academic:
        formacion_academica = input("Ingrese su formacion academica: \n")
        institucion_academ = input("Ingrese el nombre de la institucion en la que hizo esta formacion: \n ")
        titulo = input("Ingrese el titulo otorgado de esta formacion: \n")
        años_academicos = input("Ingrese en que año terminó esta formacion:  \n")
        mas_formaciones = input("Tiene mas formaciones? (si/no) \n")

        formaciones_aca[formacion_academica] = {
            "formacion" : formacion_academica,
            "institucion" : institucion_academ,
            "titulo" : titulo,
            "años" : años_academicos
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

        agregar_mas_exp = input("Desea agregar mas experiencia? ( si/no) \n")
        if agregar_mas_exp == "si":
            print("")
        elif agregar_mas_exp == "no":
            experiencias.append(diccionario_experiencia)
            ingresar_mas_experiencia = False
    elif exp_profesional == "no":
        print("no")
        ingresar_mas_experiencia =False
    


referencias_pregunta = input("tiene referencias laborales o personales? (si/no) \n")
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
    "habilidades"   : lista_habilidades

}

