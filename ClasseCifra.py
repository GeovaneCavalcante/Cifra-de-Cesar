class CifraCesar(object):

    def __init__(self, menssagem):
        # Tupla para Alfabeto
        self.codifica = (
            "abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyz", )
        self.lista = []  # Lista iniciada vazia
        self.menssagem = menssagem  # Menssagem enviada

    def encontra(self):  # Encontra a letra e sua posição
        for x in self.menssagem:
            cont = 0
            if (x == self.codifica[0][cont]):
                self.encripita(cont)
            elif (x == " "):
                a = " "
                self.encripita(a)
            else:
                while (x != self.codifica[0][cont]):
                    cont += 1
                self.encripita(cont)

    def encripita(self, letraen):  # Faz a encriptação
        numero = letraen
        if (numero == " "):
            self.lista.append("#")
        else:
            self.lista.append(self.codifica[0][numero + 3])

    def encontra2(self):
        for x in self.menssagem:
            cont = 0
            if (x == self.codifica[0][cont]):
                self.desencriptar(cont)
            elif (x == "#"):
                a = "#"
                self.desencriptar(a)
            else:
                while (x != self.codifica[0][cont]):
                    cont += 1
                self.desencriptar(cont)

    def desencriptar(self, letraen):
        numero = letraen
        if (numero == "#"):
            self.lista.append(" ")
        else:
            numero += -3
            self.lista.append(self.codifica[0][numero])

    def apresentar(self):
        palavra = ''
        contado = 0
        for x in self.lista:
            palavra += str(self.lista[contado])
            contado += 1
        print(palavra)


x = CifraCesar("geovane cavalcante")
x.encontra()  # Cifranco
x.apresentar()

x = CifraCesar("jhrydqh#fdydofdqwh")
x.encontra2()  # Decifrando
x.apresentar()
