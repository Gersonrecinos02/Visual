saludo = 25

def saludar():
    global saludo
    saludo = "hola mundo" 

    
def saludaChancito():
    saludo = "hola chancito"
    print(saludo)
    
resultado1 = saludo + 3
print(resultado1)
saludar()
resultado2 = saludo + 3
print(resultado2)


