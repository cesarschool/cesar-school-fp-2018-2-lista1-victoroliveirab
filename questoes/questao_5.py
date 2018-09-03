## QUESTÃO 5 ##
# Escreva um programa para calcular a redução do tempo de vida de um fumante. 
# Pergunte a quantidade de cigarros fumados por dia e quantos anos ele já fumou. 
# Considere que um fumante perde 10 minutos de vida a cada cigarro, calcule 
# quantos dias de vida um fumante perderá. Exiba o total em dias. 
##


##
# A sua resposta da questão deve ser desenvolvida dentro da função main()!!! 
# Deve-se substituir o comado print existente pelo código da solução.
# Para a correta execução do programa, a estrutura atual deve ser mantida,
# substituindo apenas o comando print(questão...) existente.
##
def main():
	cigarros = int(input("Quantos cigarros você fuma por dia? "))
	anos = int(input("Há quantos anos você fuma? "))
	perda = float((cigarros * anos * 365)/144) # (365 dias * 10 minutos) / (24h * 60 min) = 3650 / 1440 = 365 / 144
	print("Este fumante perdeu " + str(perda) + " dias de vida por conta do cigarro.")


    
if __name__ == '__main__':
    main()
