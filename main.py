niveldelagua=int(input("Digite el nivel del agua: "))

if niveldelagua >=0 and niveldelagua <= 250:
    print(f'el nivel del agua es muy bajo')

elif niveldelagua > 250 and niveldelagua < 450:
    print(f"El nivel del agua es estable{niveldelagua}")
    
elif niveldelagua > 450 :
    print(f'Nos vamos a morir')

else:
    print("Revisar Sensor")