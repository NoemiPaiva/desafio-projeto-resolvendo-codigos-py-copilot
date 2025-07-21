# desafio1_concat.py

nome = input("Digite seu primeiro nome: ").strip()
sobrenome = input("Digite seu sobrenome: ").strip()

if not nome or not sobrenome:
    print("Por favor, preencha todos os campos.")
else:

    nome = nome.capitalize()
    sobrenome = sobrenome.capitalize()
    
    nome_completo = f"{nome} {sobrenome}"
    
    print(f"Nome completo: {nome_completo}")