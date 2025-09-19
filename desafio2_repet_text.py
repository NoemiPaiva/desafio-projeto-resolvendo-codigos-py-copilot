# desafio2_repet_text.py

# Solicita uma string e um número inteiro
texto = input("Digite uma palavra ou frase: ")
repeticoes = int(input("Digite o número de vezes que deseja repetir: "))

# Repete o texto em linhas separadas
print("Resultado da repetição:")
for i in range(repeticoes):
    print(texto)


