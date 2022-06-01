from conta_corrente import ContaCorrente
from seguro_de_vida import SeguroDeVida
from manipulador import ManipuladorDeTributaveis
from conta_poupanca import ContaPoupanca


cc = ContaCorrente(123, "Elias", 1000)
cc.sacar(100)
cc.depositar(100)
cc.saldo()
print()
cc.valor_imposto()
cc.atualiza(0.5)

seguro = SeguroDeVida(1, 100, cc)
seguro.valor_imposto()
cc.extrato.imprime()
cc.saldo()

print("\n--------------------------------------------\n")

cp = ContaPoupanca(555, "Jordan", 5000)
cp.saldo()
print()
cp.sacar(2000)
cp.depositar(1562)
cp.atualiza(0.05)


seguro2 = SeguroDeVida(2, 1500, cp)
seguro2.valor_imposto()
cp.extrato.imprime()
cp.saldo()

print("\n--------------------------------------------\n")

cc2 = ContaCorrente(321, "Fagner", 1000)

seguro3 = SeguroDeVida(3, 350, cc2)

cc2.saldo()

manipulador = ManipuladorDeTributaveis()
tributos = [cc2, seguro3]
manipulador.calcular_impostos(tributos)

cc2.extrato.imprime()
cc2.saldo()