from conta_corrente import ContaCorrente
from tributavelmixin import TributavelMixIn


cc = ContaCorrente("Elias", 1000, 123)
tributo_mix = TributavelMixIn

print(tributo_mix.valor_imposto(0, cc))