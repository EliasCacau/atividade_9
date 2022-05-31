class Conta:
    _total_contas = 0

    def __init__(self, titular, saldo, numero):
        self._numero = Conta._total_contas + 1
        self._titular = titular
        self._saldo = saldo
        self._numero = numero
        self._contas = []
        Conta._total_contas += 1

    def depositar(self, valor):
        self._saldo += valor

    def sacar(self, valor):
        self._saldo -= valor

    def contas(self):
        self._contas.append(self._numero)
        self._contas.append(self._titular)
        self._contas.append(self._saldo)
        return self._contas
