class Livro:
    def __init__(self, titulo, autor, numero_paginas, pagina_atual):
        self.titulo = titulo
        self.autor = autor
        self.numero_pagina = numero_paginas
        self.pagina_atual = pagina_atual 

    def abrir_livro(self):
        self.pagina_atual +=1

    def ler_paginas(self, quantidade):
        self.pagina_atual += quantidade

    def exibir_progresso(self,total):
        print(" digite o numero total de paginas do livro: ", self.numero_paginas) 
        self.numero_paginas = self.numero_paginas
        total = self.numero_paginas - self.pagina_atual


class Contabancaria:
    def __init__ (self, titular, saldo, numero_conta):
        self.titular = titular
        self.saldo = saldo
        self.numero_conta

    def depositar(self, valor):
        self.saldo + vaor

    def sacar( self, valor):
        if self.saldo < valor:
            raise ValueError( "quantidade insuficiente")
        self.saldo = self.saldo - valor

    def consultar_saldo(self):
        print(" seu saldo é de : ", self.saldo)

    def exibir_dados(self, nemeroconta):
        print(" nome do titular da conta :", self.titular)
        print(" o sado da conta é de: ", self.saldo)
        print(" o numero da conta é de: ",numeroconta)
        
