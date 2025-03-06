import os
import time
import random
from colorama import Fore, Style

def inicializarJogo():
    """Inicializa ou reinicia as variáveis do jogo."""
    global jogadas, quemJoga, vit, velha
    jogadas = 0
    quemJoga = 1  # Alterna entre 1 (X) e 2 (O)
    vit = "n"  # Verificar Vitória

    velha = [
        [" ", " ", " "],
        [" ", " ", " "],
        [" ", " ", " "]
    ]

inicializarJogo()  # Inicia o jogo

def tela():
    """Exibe o tabuleiro no terminal."""
    os.system("cls" if os.name == "nt" else "clear")

    print("\n    0   1   2")
    print("0   " + velha[0][0] + " | " + velha[0][1] + " | " + velha[0][2])
    print("   -----------")
    print("1   " + velha[1][0] + " | " + velha[1][1] + " | " + velha[1][2])
    print("   -----------")
    print("2   " + velha[2][0] + " | " + velha[2][1] + " | " + velha[2][2])
    
    print("Jogadas: " + Fore.GREEN + str(jogadas) + Style.RESET_ALL)

def verificarVitoria():
    """Verifica se há um vencedor e retorna 'X', 'O' ou 'n' (ninguém venceu ainda)."""
    for i in range(3):
        # Verifica linhas e colunas
        if velha[i][0] == velha[i][1] == velha[i][2] and velha[i][0] != " ":
            return velha[i][0]
        if velha[0][i] == velha[1][i] == velha[2][i] and velha[0][i] != " ":
            return velha[0][i]

    # Verifica diagonais
    if velha[0][0] == velha[1][1] == velha[2][2] and velha[0][0] != " ":
        return velha[0][0]
    if velha[0][2] == velha[1][1] == velha[2][0] and velha[0][2] != " ":
        return velha[0][2]

    return "n"  # Nenhum vencedor ainda

def jogadorJoga():
    """Permite que o jogador escolha uma posição válida para jogar."""
    global jogadas, quemJoga

    while True:
        try:
            linha = int(input("Escolha a linha (0, 1 ou 2): "))
            coluna = int(input("Escolha a coluna (0, 1 ou 2): "))

            if linha < 0 or linha > 2 or coluna < 0 or coluna > 2:
                print(Fore.RED + "Posição inválida! Escolha entre 0, 1 e 2." + Style.RESET_ALL)
                continue

            if velha[linha][coluna] == " ":
                velha[linha][coluna] = "X" if quemJoga == 1 else "O"
                jogadas += 1
                break
            else:
                print(Fore.RED + "Posição já ocupada! Escolha outra." + Style.RESET_ALL)

        except ValueError:
            print(Fore.RED + "Entrada inválida! Digite um número entre 0 e 2." + Style.RESET_ALL)

def alternarJogador():
    """Alterna entre jogador X e jogador O."""
    global quemJoga
    quemJoga = 1 if quemJoga == 2 else 2

def finalizarJogo(mensagem):
    """Exibe a mensagem de fim do jogo e pergunta se deseja reiniciar."""
    global jogarNovamente
    tela()
    print(Fore.YELLOW + mensagem + Style.RESET_ALL)
    time.sleep(2)  # Aguarda 2 segundos antes de perguntar

    while True:
        jogarNovamente = input("\nPressione 'r' para reiniciar ou 's' para sair: ").strip().lower()
        if jogarNovamente == "r":
            inicializarJogo()
            break
        elif jogarNovamente == "s":
            exit()
        else:
            print(Fore.RED + "Opção inválida! Pressione 'r' para jogar novamente ou 's' para sair." + Style.RESET_ALL)

# Loop do jogo
while True:
    while jogadas < 9:
        tela()
        print(f"\nVez do jogador {'X' if quemJoga == 1 else 'O'}")
        jogadorJoga()

        # Verifica se há um vencedor
        vencedor = verificarVitoria()
        if vencedor != "n":
            finalizarJogo(f"\nParabéns! O jogador '{vencedor}' venceu!")
            break

        alternarJogador()

    # Se todas as jogadas forem feitas e ninguém vencer, é empate
    if verificarVitoria() == "n":
        finalizarJogo("\nEmpate! O jogo terminou sem vencedor.")
