hoja_de_vida = {}
diccionario = {}
formaciones = []
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

        diccionario[formacion_academica] = {
            "formacion" : formacion_academica,
            "institucion" : institucion_academ,
            "titulo" : titulo,
            "años" : años_academicos
         }
        

        if mas_formaciones == "si":
            print("")
        elif mas_formaciones == "no":
            formaciones.append(diccionario)
            mas_formaciones_academic = False
elif pregunt_formacion_academica == "no":
    print("no tiene formacion academica")


ingresar_mas_experiencia = True
while ingresar_mas_experiencia:
    exp_profesional  = input("Tiene experiencia en el ambito laboral? (si/no)\n")
    if exp_profesional == "si":
        experiencia = input("Ingrese su experiencia: ")
        empresas = input("Ingrese en que empresa adquirió la experiencia  \n")
        cargo = input("Ingrese el cargo que tenía en esta empresa \n ") 
        funcion = input("Ingrese la funcion que cumplia en esta empresa: \n")
        agregar_mas_exp = input("Desea agregar mas experiencia? ( si/no) \n")
        if agregar_mas_exp == "si":
            print("")
        elif agregar_mas_exp == "no":
            ingresar_mas_experiencia = False
    elif exp_profesional == "no":
        print("no")
        ingresar_mas_experiencia =False
    
referencias = input("tiene referencias laborales o personales? (si/no) \n")
if referencias == "si":


    


