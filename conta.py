#from historico import Historico
import abc


class Conta(abc.ABC):
    def __init__(self, numero, titular, saldo):
        self._numero = numero
        self._titular = titular
        self._saldo = saldo
        #self._extrato = Historico()

    @abc.abstractmethod
    def atualiza(self, taxa):
        pass

    @property
    def saldo(self):
        return print(self._saldo)

    @abc.abstractmethod
    def depositar(self, valor):
        #self._saldo += valor
        pass

    @abc.abstractmethod
    def sacar(self, valor):
        # self._saldo -= valor
        pass

    # def contas(self):
    #     # self._contas.append(self._numero)
    #     # self._contas.append(self._titular)
    #     # self._contas.append(self._saldo)
    #     # return self._contas
    #     pass
