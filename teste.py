from conta_corrente import ContaCorrente
from tributavelmixin import TributavelMixIn

conta_corrente = ContaCorrente
cc = ContaCorrente("Elias", 1000, 123)
print(conta_corrente.valor_imposto(1))