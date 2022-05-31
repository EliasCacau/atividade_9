from conta import Conta
from manipulador import ManipuladorDeTributaveis
from tributavelmixin import TributavelMixIn


class ContaCorrente(Conta, TributavelMixIn, ManipuladorDeTributaveis):
    def __init__(self, numero, titular, saldo):
        super().__init__(numero, titular, saldo)
        #self._extrato = Historico()

    def atualiza(self, taxa):
        valor = self._saldo * taxa * 2
        self.depositar(valor)
        self.sacar(0.1)
        return valor

    def saldo(self):
        return print(self._saldo)

    def depositar(self, valor):
        self._saldo += valor

    def sacar(self, valor):
        self._saldo -= valor

    def valor_imposto(self):
        ContaCorrente.sacar(self, self._saldo * 0.02)
        return ContaCorrente.saldo(self)

