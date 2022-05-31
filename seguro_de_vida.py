from tributavelmixin import TributavelMixIn


class SeguroDeVida(TributavelMixIn):
    def __init__(self, numero, valor, titular):
        self._numero = numero
        self._valor = valor
        self._titular = titular

    def valor_seguro(self):
        self._titular.sacar(self._valor + self._valor * 0.05 + 34)
        return print(f"Valor do seguro: {self._valor + self._valor * 0.05 + 34} \nTotal na conta:", end=" "), self._titular.saldo()

    def valor_imposto(self):
        pass