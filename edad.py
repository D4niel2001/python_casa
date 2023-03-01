edad = int(input('Digite tu edad actualmente:'))

if edad >= 0 and edad <= 14:
    print(f'a tus {edad} anos tienes la edad de un nino')

elif edad >= 15 and edad <= 28:
    print(f'a tus {edad} anos tienes la edad de un joven')

elif edad >= 29 and edad <= 60:
    print(f'a tus {edad} anos ya eres una persona adulta')

elif edad > 60:
    print(f'a tus{edad} anos ya eres un adulto mayor :v')
    exit()
    