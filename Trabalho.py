import random

numero = random.randint(1,100)
chute = 0

print('Tente advinhar o número entre 1 e 100.')

dificuldade = {
1: 10,
2: 5,
3:3,

}

print("""
Escolha a dificuldade:
1.  Facil
2. Medio
3. Dificil
""")

d = int(input('Insira a dificuldade [1/2/3]: '))
n_de_tentativas = dificuldade[d]
tentativa = 1
while tentativa < n_de_tentativas :
    
    chute = int(input('Introduza a sua tentativa: '))

    if numero == chute:
        print('Parabéns, você acertou o número!')
        break
    else:
        if numero < chute:
            print('O número é menor que a sua tentativa.')
        if numero > chute:
            print('O número é maior que a sua tentativa.')
else:
    print("Infelizmente vc usou todas as tentativas!")