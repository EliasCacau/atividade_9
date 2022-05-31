import abc

class Conta(abc.ABC):
    def __init__(self, n, cli, sal):
        self._numero = n
        self._titular = cli
        self._saldo = sal
        self._extrato = Historico()

    def atualiza(self, taxa):
        pass

    def saldo(self):
        #return self._saldo
        pass

    def depositar(self, valor):
        #self._saldo += valor
        pass

    def sacar(self, valor):
        # self._saldo -= valor
        pass

    # def contas(self):
    #     # self._contas.append(self._numero)
    #     # self._contas.append(self._titular)
    #     # self._contas.append(self._saldo)
    #     # return self._contas
    #     pass
