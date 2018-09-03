## QUESTÃO 1 ## 
# Faça um programa que calcule o aumento de um salário. Ele deve solicitar o 
# valor do salário e a porcentagem do aumento. Exiba o valor do aumento e do 
# novo salário. 
##

##
# A sua resposta da questão deve ser desenvolvida dentro da função main()!!! 
# Deve-se substituir o comado print existente pelo código da solução.
# Para a correta execução do programa, a estrutura atual deve ser mantida,
# substituindo apenas o comando print(questão...) existente.
##
def main():
    salario = int(input("Informe seu salario: "))
    aumento = int(input("Informe o seu aumento percentual: "))
    aumento = aumento*salario/100
    salario += aumento
    print("Seu novo salario é " + str(salario) + " por conta de um aumento de " + str(aumento))
    


if __name__ == '__main__':
    main()