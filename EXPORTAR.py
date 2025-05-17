import os

def exportar_hoja_txt(num_id, hoja_de_vida):
    if num_id not in hoja_de_vida:
        print("No se encontró la hoja de vida con esa cédula.")
        return
    
    datos = hoja_de_vida[num_id]
    carpeta = "Hojas_de_Vida"
    if not os.path.exists(carpeta):
        os.makedirs(carpeta)
    
    nombre_archivo = f"{carpeta}/HDV_{num_id}.txt"
    with open(nombre_archivo, "w", encoding="utf-8") as f:
        f.write("========== HOJA DE VIDA ==========\n")
        f.write(f"Nombre: {datos['nombre']}\n")
        f.write(f"Cédula: {num_id}\n")
        f.write(f"Fecha de nacimiento: {datos['fecha nacimiento'].strftime('%d/%m/%Y')}\n")
        f.write(f"Correo: {datos['correo']}\n")
        f.write(f"Contacto: {datos['contacto']}\n")
        f.write(f"Dirección: {datos['direccion']}\n\n")

        f.write("Formación académica\n")
        if datos["formaciones"]:
            for formacion_dict in datos["formaciones"]:
                for _, formacion in formacion_dict.items():
                    f.write(f"- {formacion['formacion']} en {formacion['institucion']} - Título: {formacion['titulo']} ({formacion['aÃ±os']})\n")
        else:
            f.write("No registra formaciones académicas.\n")
        f.write("\n")

        f.write("Experiencia profesional\n")
        if datos["experiencias"]:
            for experiencia_dict in datos["experiencias"]:
                for _, exp in experiencia_dict.items():
                    f.write(f"- {exp['cargo']} en {exp['empresa']} ({exp['duracion']})\n")
                    f.write(f"  Funciones: {exp['funcion']}\n")
        else:
            f.write("No registra experiencia laboral.\n")
        f.write("\n")

        f.write("Personas a las que se le refiere\n")
        if datos["referencias"]:
            for ref, info in datos["referencias"].items():
                f.write(f"- {ref} ({info['relacion']}) - {info['contacto']}\n")
        else:
            f.write("No registra referencias.\n")
        f.write("\n")

        f.write("Habilidades\n")
        if datos["habilidades"]:
            f.write(", ".join(datos["habilidades"]) + "\n")
        else:
            f.write("No registra habilidades.\n")

    print(f"Hoja de vida exportada como '{nombre_archivo}'")