import os 
import random
import globales

def montos_aleatorios():
    total_datos = globales.leer_archivo_json('datos.json')
    productos = ["Cafe Americano", "Te Chai", "Croissant", "Jugo Naranja", "Panini de Pavo y Queso", "Pastel de Zanahoria", "Espresso Doble", "Batido de Frutas", "Muffin", "Ensalada", "Chocolate Caliente", "Tarta de Frambuesa", "Sandwich de Huevo", "Galletas de Avena", "Frappe de Caramelo"]

    for i in range(15):
        i+=1
        nombre_producto = random.choice(productos)
        valor_productos = random.randint(2000, 10000)

        nuevo_producto = {
            "nombre": productos,
            "valor": valor_productos,
            "iva": valor_productos*0.19
        }

        total_datos.append(nuevo_producto)

    globales.guardar_archivo_json('datos.json',total_datos)
    print("Variables Cargadas")