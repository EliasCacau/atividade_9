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