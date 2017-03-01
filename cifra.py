# Alfabeto
codifica = ["abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyz", ]
lista = []  # Lista iniciada vazia
val = 0  # opção do user

# Ler a menssagem

def lermen():
    menssagem = str(input("Digite a menssagem para cripitografa: "))
    return menssagem

# Encontra a letra

def encontra():
    menssagem = lermen()
    for x in menssagem:
        cont = 0
        if (x == codifica[0][cont]):
            descobreposição(codifica[0][cont])
        elif (x == " "):
            a = " "
            descobreposição(a)
        else:
            while (x != codifica[0][cont]):
                cont += 1
            descobreposição(codifica[0][cont])

# Encontra a posição da letra no alfabeto

def descobreposição(letra):
    for x in letra:
        cont = 0
        if (x == codifica[0][cont]):
            cont = cont
            encripita(cont)
        elif (x == " "):
            a = " "
            encripita(a)
        else:
            while (x != codifica[0][cont]):
                cont += 1
            encripita(cont)

# Ecripta a letra adicionando a mesma em uma lista

def encripita(numero):
    if (numero == " "):
        lista.append("#")
    else:
        lista.append(codifica[0][numero + 3])

# Transformando a lista em String

def apresentar():
    palavra = ''
    contado = 0
    for x in lista:
        palavra += str(lista[contado])
        contado += 1
    print(palavra)


def menu():
    print("\tAlgoritmo de Cifra de César\n")
    print("\tDigite 1 para encriptar um código: ")
    print("\tDigite 2 para desecriptar um código: ")
    val = int(input("\t Qual opção desejada? "))
    if (val == 1):
        encontra()
        apresentar()
    elif (val == 2):
        print('')


menu()
