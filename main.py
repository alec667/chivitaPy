from random import randint

animales = ["el lobo", "el toro", "el perro", "el leon"]

N = int(input("enter N: "))
llamarA = {}

print("Sal de ahí chivita chivita, sal de ahí de ese lugar")
act = "la chiva"
for i in range(N):
    prox = animales[randint(0, len(animales) - 1)]
    llamarA[act] = prox
    print(f"Hay que llamar a {prox} para que saque a {act}")
    act = prox
    remover = []
    inspeccionar = "la chiva"
    while inspeccionar in llamarA:
        remover.insert(0, llamarA[inspeccionar] + " no quiere sacar a " + inspeccionar)
        inspeccionar = llamarA[inspeccionar]

    for index in remover:
        print(index)

    print("La chiva no quiere salir de ahí. Sal de ahí chivita chivita, sal de ahí de ese lugar")
