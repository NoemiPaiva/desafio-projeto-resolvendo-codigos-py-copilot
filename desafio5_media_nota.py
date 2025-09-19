# desafio5_media_nota.py

#Primeira sugestão de código
# Solicita três notas ao usuário
"""
nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))
nota3 = float(input("Digite a terceira nota: "))

# Calcula a média
media = (nota1 + nota2 + nota3) / 3

# Exibe o resultado
print(f"A média das notas é: {media:.2f}")
"""

# Segunda Sugestão de código


# Introdução
print("📚 Cálculo de Média Escolar")
print("Informe suas três notas para saber sua média final.")

# Entrada de dados
nome = input("Digite seu nome: ")
nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))
nota3 = float(input("Digite a terceira nota: "))

# Cálculo da média
media = (nota1 + nota2 + nota3) / 3

# Exibição do resultado com contexto
print(f"\nAluno(a): {nome}")
print(f"Notas: {nota1}, {nota2}, {nota3}")
print(f"Média final: {media:.2f}")

# Avaliação simples
if media >= 7:
    print("Situação: ✅ Aprovado(a)")
else:
    print("Situação: ❌ Reprovado(a)")


