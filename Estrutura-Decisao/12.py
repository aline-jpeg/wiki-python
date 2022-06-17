''''
Faça um programa para o cálculo de uma folha de pagamento, sabendo que os
descontos são do Imposto de Renda, que depende do salário bruto
(conforme tabela abaixo) e 10% para o INSS e que o FGTS corresponde a 11% do
Salário Bruto, mas não é descontado (é a empresa que deposita).
O Salário Líquido corresponde ao Salário Bruto menos os descontos.
O programa deverá pedir ao usuário o valor da sua hora e a quantidade de horas
trabalhadas no mês.

Desconto do IR:
    Salário Bruto até 900 (inclusive) - isento
    Salário Bruto até 1500 (inclusive) - desconto de 5%
    Salário Bruto até 2500 (inclusive) - desconto de 10%
    Salário Bruto acima de 2500 - desconto de 20%

Imprima na tela as informações, dispostas conforme o exemplo abaixo.
No exemplo o valor da hora é 5 e a quantidade de hora é 220.
        Salário Bruto: (5 * 220)        : R$ 1100,00
        (-) IR (5%)                     : R$   55,00
        (-) INSS ( 10%)                 : R$  110,00
        FGTS (11%)                      : R$  121,00
        Total de descontos              : R$  165,00
        Salário Liquido                 : R$  935,00
'''

valor = float(input('Valor hora trabalhada: R$'))

hora = int(input('Horas trabalhadas: '))

salarioBruto = valor * hora

if salarioBruto <= 900:
    ir = 0.0
elif salarioBruto <= 1500:
    ir = 5
elif salarioBruto <= 2500:
    ir = 10
else:
    ir = 20


IR = salarioBruto * (ir / 100)
INSS = salarioBruto * (10 / 100)
FGTS = salarioBruto* (11 / 100)
descontos = IR + INSS
salarioLiquido = salarioBruto - descontos

print(
    f"\nSalário Bruto     : R${salarioBruto:.2f}",
    f"\n(-) IR (5%)       : R${IR:.2f}",
    f"\n(-) INSS ( 10%)   : R${INSS:.2f}",
    f"\nFGTS (11%)        : R${FGTS:.2f}",
    f"\nTotal de descontos: R${descontos:.2f}",
    f"\nSalário Liquido   : R${salarioLiquido:.2f}",
)