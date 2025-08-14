# Classe que representa um livro
class Livro:
    def __init__(self, titulo, autor, numero_paginas, pagina_atual):
        # Armazena as informações básicas do livro
        self.titulo = titulo
        self.autor = autor
        self.numero_paginas = numero_paginas  # Corrigi o nome da variável (estava numero_pagina)
        self.pagina_atual = pagina_atual

    # Simula abrir o livro avançando 1 página
    def abrir_livro(self):
        self.pagina_atual += 1

    # Simula a leitura de várias páginas
    def ler_paginas(self, quantidade):
        self.pagina_atual += quantidade

    # Mostra o progresso da leitura
    def exibir_progresso(self):
        # Calcula quantas páginas faltam para terminar o livro
        paginas_restantes = self.numero_paginas - self.pagina_atual
        print("Total de páginas do livro:", self.numero_paginas)
        print("Página atual:", self.pagina_atual)
        print("Páginas restantes:", paginas_restantes)


# Classe que representa uma conta bancária
class ContaBancaria:
    def __init__(self, titular, saldo, numero_conta):
        # Armazena as informações básicas da conta
        self.titular = titular
        self.saldo = saldo
        self.numero_conta = numero_conta

    # Adiciona dinheiro à conta
    def depositar(self, valor):
        self.saldo += valor  # Corrigi "vaor" para "valor"

    # Retira dinheiro da conta, se houver saldo suficiente
    def sacar(self, valor):
        if self.saldo < valor:
            raise ValueError("Quantidade insuficiente")
        self.saldo -= valor

    # Mostra o saldo atual
    def consultar_saldo(self):
        print("Seu saldo é de:", self.saldo)

    # Mostra as informações da conta
    def exibir_dados(self):
        print("Nome do titular da conta:", self.titular)
        print("Saldo da conta:", self.saldo)
        print("Número da conta:", self.numero_conta)
