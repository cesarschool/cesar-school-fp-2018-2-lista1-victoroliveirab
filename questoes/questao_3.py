## QUESTÃO 3 ##
# Escreva um programa que calcule a área de um círculo, o diâmetro e o comprimento 
# da circunferência. Solicite que o usuário insira o raio e imprima uma mensagem 
# agradável de volta para o usuário com a resposta. 
##

##
# A sua resposta da questão deve ser desenvolvida dentro da função main()!!! 
# Deve-se substituir o comado print existente pelo código da solução.
# Para a correta execução do programa, a estrutura atual deve ser mantida,
# substituindo apenas o comando print(questão...) existente.
##
def main():
    from math import pi
    R = float(input("Insira do raio da circunferência desejada: "))
    area = pi * R**2
    d = 2*R
    comprimento = 2*pi*R
    print("Uma circunferência de raio " + str(R) + " tem as seguintes propriedades:\nArea = " + str(area) + "\nDiâmetro = " + str(d) + "\nComprimento = " + str(comprimento) + "\nObrigado pela confiança :P")


    
if __name__ == '__main__':
    main()
