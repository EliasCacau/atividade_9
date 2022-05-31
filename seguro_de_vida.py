from tributavelmixin import TributavelMixIn


class SeguroDeVida(TributavelMixIn):
    def __init__(self, numero, valor, titular):
        self._numero = numero
        self._valor = valor
        self._titular = titular

    def valor_imposto(self, conta):
        pass