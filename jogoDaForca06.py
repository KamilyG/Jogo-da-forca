# by Kamily and Viccenzo

import os

def desenhaForca(erros):
    print("  _______     ")
    print(" |/      |    ")

    if(erros == 1):
        print(" |      (_)   ")
        print(" |            ")
        print(" |            ")
        print(" |            ")

    if(erros == 2):
        print(" |      (_)   ")
        print(" |       |    ")
        print(" |       |    ")
        print(" |            ")

    if(erros == 3):
        print(" |      (_)   ")
        print(" |      \|   ")
        print(" |       |    ")
        print(" |            ")

    if(erros == 4):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |            ")

    if(erros == 5):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      /     ")

    if (erros == 6):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      / \   ")

    print(" |            ")
    print("_|___         ")
    print()

def abrirArquivo():
    abrir = open("resultados.txt", "a")
    abrir.close()

def lerArquivos():
    arquivo = open("resultados.txt","r")
    conteudo = arquivo.read()
    arquivo.close()
    return conteudo

alfabeto = list("abcdefghijklmnopqrstuvwxyz")

try:
    abrirArquivo()
except:
    lerArquivos()

def main():

    vencedor = ''
    perdedor = ''
    
    def gravarArquivos():
        arquivo = open("resultados.txt","a")
        linhasParaOArquivo = ["Palavra-chave: ", palavraChave," - Vencedor: ", vencedor, " - Perdedor: ", perdedor + "\n"]
        for lnh in linhasParaOArquivo:
            arquivo.write(lnh)
        arquivo.close()

    def mudaEstadoAtual():
        for i in range(len(palavraChave)):
            if letra == palavraChave[i]:
                estadoAtual[i] = letra

    def tentaUmaLetra():
        while True:
            letra = str(input("Digite uma letra.\n"))
            if letra in alfabeto:
                if letra in digitadas:
                    print("Você já tentou esta letra!")
                    continue
                else:
                    digitadas.append(letra)
            else:
                print("Isso não é letra!")
                continue
            return letra

    lerHistorico = lerArquivos()

    desafiante = str(input("Desafiante: " ))
    competidor = str(input("Competidor: " ))
    os.system("cls")

    print(desafiante +", responda as perguntas a seguir.\n ATENÇÂO! Não deixe que o competidor veja.")
    palavraChave = str(input("Digite uma palavra-chave: "))
    
    dica1 = ''
    dica2 = ''
    dica3 = ''

    while dica1 == '':
        print("Por favor, preencha a primeira dica.")
        dica1 = str(input("Digite a primeira dica 1: "))
    while dica2 == '':
        print("Por favor, preencha a segunda dica.")
        dica2 = str(input("Digite a segunda dica 2: "))
    while dica3 == '':
        print("Por favor, preencha a terceira dica.")
        dica3 = str(input("Digite a terceira dica 3: "))
      
    os.system("cls")

    estadoAtual = ["*" for _ in range(len(palavraChave))]
    dicas = [dica1, dica2, dica3]
    dicasCont = 0
    digitadas = []
    erros = 0

    while True:
        print ("A palavra contém",len(palavraChave),"letras.\n",estadoAtual)
        print(competidor +", o que você deseja fazer?")
        print("(1) Jogar")
        print("(2) Solicitar Dica")
        print("(3) Sair")
        op = input()
        op2 = 0
        if op == "1":
            print("Letras digitadas: "+ str(digitadas).strip('[]'))
            letra = tentaUmaLetra()
            if len(letra) == 1:
                os.system("cls")
                if letra in palavraChave:
                    mudaEstadoAtual()
                    print("Você acertou a letra!")
                    if "*" not in estadoAtual:
                        vencedor = competidor
                        perdedor = desafiante
                        gravarArquivos()
                        while True:
                            print("Histórico de jogos:\n"+lerHistorico)
                            print("Resultado da partida:\nPalavra-chave: ", palavraChave," - Vencedor: ", vencedor, " - Perdedor: ", perdedor + "\n")
                            print(competidor+", você ganhou!")
                            print("O que você deseja fazer?")
                            print("(1) Jogar novamente")
                            print("(2) Sair")
                            op2 = input()
                            if op2 == "1":
                                main()
                            elif op2 == "2":
                               exit()
                            else:
                                print("Carácter inválido!")

                elif letra not in palavraChave:
                    erros = erros + 1
                    print("A palavra não tem essa letra.\n Erro:", erros)
                    desenhaForca(erros)
                    if erros > 5:
                        vencedor = desafiante
                        perdedor = competidor
                        gravarArquivos()
                        while True:
                            print("Histórico de jogos:\n"+lerHistorico)
                            print("Resultado da partida:\nPalavra-chave: ", palavraChave," - Vencedor: ", vencedor, " - Perdedor: ", perdedor + "\n")
                            print(competidor+", você perdeu!")
                            print("O que você deseja fazer?")
                            print("(1) Jogar novamente")
                            print("(2) Sair")
                            op2 = input()
                            os.system("cls")
                            if op2 == "1":
                                main()
                            elif op2 == "2":
                               exit()
                            else:
                                print("Carácter inválido!")
                       
            else:
                print("ERRO! Só é permitido digitar uma letra.")
                print("Letras digitadas: " + str(digitadas).strip('[]'))
                letra = tentaUmaLetra()
                if len(letra) == 1:
                    os.system("cls")
                    if letra in palavraChave:
                        mudaEstadoAtual()
                        if "*" not in estadoAtual:
                            vencedor = competidor
                            perdedor = desafiante
                            gravarArquivos()
                            while True:
                                print("Histórico de jogos:\n"+lerHistorico)
                                print(competidor+", você ganhou!")
                                print("Resultado da partida:\nPalavra-chave: ", palavraChave," - Vencedor: ", vencedor, " - Perdedor: ", perdedor + "\n")
                                print("O que você deseja fazer?")
                                print("(1) Jogar novamente")
                                print("(2) Sair")
                                op2 = input()
                                os.system("cls")
                                if op2 == "1":
                                    main()
                                elif op2 == "2":
                                    exit()
                                else:
                                    print("Carácter inválido!")

                    elif letra not in palavraChave:
                        erros = erros + 1
                        print("A palavra não tem essa letra.\n Erro:", erros)
                        desenhaForca(erros)
                        if erros > 5:
                            vencedor = desafiante
                            perdedor = competidor
                            gravarArquivos()
                            while True:
                                print("Histórico de jogos:\n"+lerHistorico)
                                print("Resultado da partida:\nPalavra-chave: ", palavraChave," - Vencedor: ", vencedor, " - Perdedor: ", perdedor + "\n")
                                print(competidor+", você perdeu!")
                                print("O que você deseja fazer?")
                                print("(1) Jogar novamente")
                                print("(2) Sair")
                                op2 = input()
                                os.system("cls")
                                if op2 == "1":
                                    main()
                                elif op2 == "2":
                                    exit()
                                else:
                                    print("Carácter inválido!")   
            
        elif op == "2":
            if dicasCont > 2:
                print("Você não tem mais dicas!")
            else:
                print("Dica: " + dicas[dicasCont])
                dicasCont = dicasCont + 1

            print("Letras digitadas: "+ str(digitadas).strip('[]'))
            letra = tentaUmaLetra()
            if len(letra) == 1:
                    os.system("cls")
                    if letra in palavraChave:
                        mudaEstadoAtual()
                        print("Você acertou a letra!")
                        if "*" not in estadoAtual:
                            vencedor = competidor
                            perdedor = desafiante
                            gravarArquivos()
                            while True:
                                print("Histórico de jogos:\n"+lerHistorico)
                                print("Resultado da partida:\nPalavra-chave: ", palavraChave," - Vencedor: ", vencedor, " - Perdedor: ", perdedor + "\n")
                                print(competidor+", você ganhou!")
                                print("O que você deseja fazer?")
                                print("(1) Jogar novamente")
                                print("(2) Sair")
                                op2 = input()
                                os.system("cls")
                                if op2 == "1":
                                    main()
                                elif op2 == "2":
                                    exit()
                                else:
                                    print("Carácter inválido!")                                            

                    elif letra not in palavraChave:
                        erros = erros + 1
                        print("A palavra não tem essa letra.\n Erro:", erros)
                        desenhaForca(erros)
                        if erros > 5:
                            vencedor = desafiante
                            perdedor = competidor
                            gravarArquivos()
                            while True:
                                print("Histórico de jogos:\n"+lerHistorico)
                                print("Resultado da partida:\nPalavra-chave: ", palavraChave," - Vencedor: ", vencedor, " - Perdedor: ", perdedor + "\n")
                                print(competidor+", você perdeu!")
                                print("O que você deseja fazer?")
                                print("(1) Jogar novamente")
                                print("(2) Sair")
                                op2 = input()
                                os.system("cls")
                                if op2 == "1":
                                    main()
                                elif op2 == "2":
                                    exit()
                                else:
                                    print("Carácter inválido!")

        elif op == "3":
            exit()

        else:
            print("Carácter inválido!")
main()