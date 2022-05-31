from conta_corrente import ContaCorrente
from tributavelmixin import TributavelMixIn
from seguro_de_vida import SeguroDeVida

conta_corrente = ContaCorrente
cc = ContaCorrente(123, "Elias", 1000)
cc.sacar(100)
cc.depositar(100)
cc.saldo()
cc.valor_imposto()

seguro = SeguroDeVida(1, 100, cc)
seguro.valor_seguro()

cc.depositar(15)
cc.saldo()