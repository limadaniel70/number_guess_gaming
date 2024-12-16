import random
import sys

numero = random.randint(1, 100)

print('Tente advinhar o número entre 1 e 100.')

dificuldades = [
    ("Fácil", 10),
    ("Medio", 5),
    ("Difícil", 3),
    ("Impossível", 1)
]

print("""
Escolha a dificuldade:
1. Fácil        (10 tentativa(s))
2. Medio        (5  tentativa(s))
3. Difícil      (3  tentativa(s))
4. Impossível   (1  tentativa(s))
""")

print('Insira a dificuldade [1/2/3/4]')
try:
    nivel = int(input("> "))

    if nivel < 1 or nivel > 4:
        raise ValueError

except TypeError:
    print("O valor precisa ser um número!")
    sys.exit(1)
except ValueError:
    print("Por favor, insira um valor válido")
    sys.exit(1)

nivel, tentativas = dificuldades[nivel - 1]
tentativa = 0

print(f"Você escolheu a dificuldade: {nivel}")
print(f"Total de tentativas: {tentativas}") 

while tentativa < tentativas:
    print("=" * 40)
    print(f"Tentativas restantes: {tentativas - tentativa}")
    chute = int(input('Introduza a sua tentativa:\n> '))
    tentativa += 1

    if numero == chute:
        print(f'Parabéns, você acertou o número em {tentativa} tentativas!')
        break
    elif numero < chute:
            print('O número é menor que a sua tentativa.')
    elif numero > chute:
            print('O número é maior que a sua tentativa.')
else:
    print("Infelizmente você usou todas as tentativas!")
