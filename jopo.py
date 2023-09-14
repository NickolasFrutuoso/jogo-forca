# Exemplo JOGO DA FORCA
# 14/09/2023
# TRABALHO - FACULDADE

# forma de 'esconder' a palavra chave
from palavraforca import palavra

letras_usuario = []  # quantidade de letras que o usario chutou
chances = 7  # ele pode errar até 7 letras
ganhou = False
print("")

# looping infinito
while True:
    print(f"\nVocê tem {chances} chances.\n")
    # para cada letra dentro da minha palavra, exiba assim _ _ _ _ _ _ _ _
    for letra in palavra:
        # se ele acertar a letra, ele ira trocar _ pela letra
        if letra.lower() in letras_usuario:
            # end, padrao python = \n, trocar para ' ' para ficar um do lado do outro
            # ex: _ _ _
            print(letra, end=" ")
        else:
            print("_ ", end="")
    # pegar uma tentativa de letra do usuario
    tentativa = input("\nEscolha uma letra: ")
    # adicionar essa letra dentro de letras, lower transforma A para a, para n ter conflito
    letras_usuario.append(tentativa.lower())
    # se nao tiver essa letra, vai tirar uma tentativa do usuario
    if tentativa.lower() not in palavra.lower():
        chances -= 1

    ganhou = True
    # para cada letra dentro da palavra, se a letra.lower() nao
    # tiver dentro da letra do usuario, entao ganhou = false
    for letra in palavra:
        if letra.lower() not in letras_usuario:
            ganhou = False

    # se as chancer for igual a 0, para o jogo = perdeu
    if chances == 0 or ganhou:
        break

# se ele ganhar
if ganhou:
    print(f"\nParabens, você ganhou. A palavra era: {palavra}\n")
# se ele perder
else:
    print(f"\nVocê perdeu! A palavra era: {palavra}\n")
