from conta import Conta


class Banco(Conta):
    def __init__(self, numero, nome, titular, saldo, limite):
        super().__init__(titular, saldo, limite)
        self._numero = numero
        self._nome = nome
        self.saldo = 0
        self._contas = []

    def get_conta(self):
        return self._contas.append(Conta.contas())
