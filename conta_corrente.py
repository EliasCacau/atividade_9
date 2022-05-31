from conta import Conta
from tributavelmixin import TributavelMixIn


class ContaCorrente(Conta, TributavelMixIn):
    def __init__(self, titular, saldo, numero):
        super().__init__(titular, saldo, numero)

    def atualiza(self, taxa):
        valor = self._saldo * taxa * 2
        self.depositar(valor)
        self.sacar(0.1)
        return valor

    def saldo(self):
        return self._saldo

    def depositar(self, valor):
        self._saldo += valor

    def sacar(self, valor):
        self._saldo -= valor
        pass

    def valor_imposto(self, conta):
        # saldo = conta.saldo()
        # taxa = (saldo - saldo * 0.2) + (saldo - saldo * 0.5) + 32
        # conta.sacar(taxa)
        return conta.saldo()