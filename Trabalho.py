import random

numero = random.randint(1, 100)

print('Tente advinhar o número entre 1 e 100.')

dificuldades = {
1: {"Dificuldade": "Fácil", "Tentativas": 10},
2: {"Dificuldade": "Medio", "Tentativas": 5},
3: {"Dificuldade": "Difícil", "Tentativas": 3},
}

print("""
Escolha a dificuldade:
1.  Facil
2. Medio
3. Dificil
""")

d = int(input('Insira a dificuldade [1/2/3]: '))

n_de_tentativas = dificuldades[d]["Tentativas"]
tentativa = 0

print(f"Você escolheu a dificuldade: {dificuldades[d]['Dificuldade']}")
print(f"Total de tentativas: {n_de_tentativas}") 

while tentativa < n_de_tentativas:
    print("-" * 40)
    print(f"Tentativas restantes: {n_de_tentativas - tentativa}")
    chute = int(input('Introduza a sua tentativa: '))
    # O erro acontecia pois a tentativa nuna
    # era aumentava.
    tentativa += 1

    if numero == chute:
        print('Parabéns, você acertou o número!')
        break
    else:
        if numero < chute:
            print('O número é menor que a sua tentativa.')
        if numero > chute:
            print('O número é maior que a sua tentativa.')
else:
    print("Infelizmente você usou todas as tentativas!")
