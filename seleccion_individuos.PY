import json

"""
Este script carga un archivo JSON que contiene una lista de individuos,
y filtra únicamente aquellos cuyos IDs están incluidos en una colección
predefinida y guarda el resultado en un nuevo archivo JSON.

Flujo general:
1. Definir los IDs que se desean conservar.
2. Leer el archivo JSON original.
3. Filtrar los elementos según su campo "id".
4. Guardar los elementos filtrados en un nuevo archivo.
5. Mostrar cuántos registros fueron guardados.
"""

# IDs que quiero conservar "15", "34", "13" , "18", "17", "16" , "40" , "14"
ids_deseados = {"15", "34", "13" , "18", "17", "16" , "40"}

# Se lee el archivo original
with open("omop2BFF_individuals.json", "r", encoding="utf-8") as f:
    data = json.load(f)

# Se filtran los individuos por id
filtrados = [persona for persona in data if persona.get("id") in ids_deseados]

# Se guardan los resultados
with open("individuals_seleccionados.json", "w", encoding="utf-8") as f:
    json.dump(filtrados, f, ensure_ascii=False, indent=4)

print(f"Se guardaron {len(filtrados)} individuos.")

