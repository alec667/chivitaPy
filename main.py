import time
from random import randint

animales = ["El lobo", "El toro", "El perro", "El león", "El caballo", "La vaca", "El gato", "El elefante", "El tigre",
            "El mono",
            "El oso", "La oveja", "El ciervo", "La cabra", "El cerdo", "El pato", "El ganso", "La gallina", "El gallo",
            "La águila", "El cuervo", "La golondrina", "El halcón", "La paloma", "El ratón", "La rata", "El búho",
            "La lechuza", "El pingüino", "El canguro", "La jirafa", "El rinoceronte", "El hipopótamo", "La ardilla",
            "El castor", "La marmota", "El zorro", "La mofeta", "El tejón", "La nutria", "El mapache", "El puma",
            "La pantera", "El guepardo", "El chacal", "La hiena", "El lémur", "La zarigüeya", "El wallaby", "El koala",
            "La tortuga", "El cocodrilo", "El caimán", "El lagarto", "La iguana", "El camaleón", "La serpiente",
            "La anaconda", "La boa", "La víbora", "El escorpión", "La araña", "El ciempiés", "El milpiés", "La hormiga",
            "La abeja", "La avispa", "El saltamontes", "La langosta", "El grillo", "La mariposa", "El gusano",
            "La oruga",
            "La libélula", "El escarabajo", "El caracol", "La babosa", "La almeja", "El mejillón", "El cangrejo",
            "La langosta2", "El camarón", "La gamba", "El pulpo", "La sepia", "El calamar", "El tiburón", "La ballena",
            "El delfín", "La foca", "El león marino", "El pingüino emperador", "La estrella de mar", "El erizo de mar",
            "La medusa", "El pez2", "El pez espada", "La manta raya", "El caballito de mar", "La anguila"]

N = int(input("enter N: "))
llamarA = {}

inicio = time.time_ns()

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
fin = time.time_ns()
print(f"-------->Tiempo de ejecución: {(fin - inicio) / 1000000} milisegundos")
