# desafio6_palindromos.py

#Solicita uma palavra ao usuário
palavra = input("Digite uma palavra para verificar se é um palíndromo: ")

# Remove espaços e transforma em minúsculas para comparação mais precisa
palavra_formatada = palavra.replace(" ", "").lower()

# Verifica se é igual à sua versão invertida
if palavra_formatada == palavra_formatada[::-1]:
    print(f"A palavra '{palavra}' é um palíndromo! 🔄")
else:
    print(f"A palavra '{palavra}' não é um palíndromo.")
