mes = input("Ingrese un mes para ver en que estacion estas:").lower()

if mes in ["enero", "febrero", "marzo"]:
    estacion = "invierno"
elif mes in ["abril", "mayo", "junio"]:
    estacion = "verano"
elif mes in ["julio", "agosto", "septiembre"]:
    estacion = "otoño"
elif mes in ["octubre", "noviembre", "diciembre"]:
    estacion = "primavera"
else:
    print("Mes ingresado no existe.")
    exit()

print(f"La estación correspondiente al mes ingresado es: {estacion}")
