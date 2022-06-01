from tributavelmixin import TributavelMixIn


class SeguroDeVida(TributavelMixIn):
    def __init__(self, numero, valor, titular):
        self._numero = numero
        self._valor = valor
        self._titular = titular

    def valor_imposto(self):
        valor = self._valor * 0.05 + 34
        self._titular.sacar(self._valor * 0.05 + 34)
        return valor
