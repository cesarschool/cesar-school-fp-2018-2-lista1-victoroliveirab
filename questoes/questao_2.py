## QUESTÃO 2 ##
# Escreva um programa que converta uma temperatura digitada em °C (graus celsius) 
# para °F (graus fahrenheit). 
##


##
# A sua resposta da questão deve ser desenvolvida dentro da função main()!!! 
# Deve-se substituir o comado print existente pelo código da solução.
# Para a correta execução do programa, a estrutura atual deve ser mantida,
# substituindo apenas o comando print(questão...) existente.
##
def main():
    c = float(input("Informe a temperatura em graus Celsius: ")) #temperatura em celsius
    f = 1.8*c + 32 #conversao para graus fahrenheit
    print("A temperatura informada corresponde a " + str(f) + " graus Fahrenheit.")



if __name__ == '__main__':
    main()
