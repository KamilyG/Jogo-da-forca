
# botar gravarArquivos fora do while

def main():

    import os

    vencedor = ''
    perdedor = ''
    
    def gravarArquivos():
        arquivo = open("resultados.txt","a")
        linhasParaOArquivo = ["Palavra-chave: ", palavraChave," - Vencedor: ", vencedor, " - Perdedor: ", perdedor + "\n"]
        for lnh in linhasParaOArquivo:
            arquivo.write(lnh)
        arquivo.close()
    
    def lerArquivos():
        arquivo = open("resultados.txt","r")
        conteudo = arquivo.read()
        arquivo.close()
        return conteudo

    def mudaEstadoAtual():
        for i in range(len(palavraChave)):
            if letra == palavraChave[i]:
                estadoAtual[i] = letra

    def tentaUmaLetra():
        letra = input("Digite uma letra.\n")
        digitadas.append(letra)
        return letra

    lerHistorico = lerArquivos()

    desafiante = str(input("Desafiante: " ))
    competidor = str(input("Competidor: " ))
    os.system("cls")

    print(desafiante +", responda as perguntas a seguir.\n ATENÇÂO! Não deixe que o competidor veja.")
    palavraChave = str(input("Digite uma palavra-chave: "))
    dica1 = str(input("Digite a primeira dica: "))
    dica2 = str(input("Digite a segunda dica: "))
    dica3 = str(input("Digite a terceira dica: "))
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
                            print(competidor+", você ganhou!")
                            print("O que você deseja fazer?")
                            print("(1) Jogar novamente")
                            print("(2) Sair")
                            op2 = input()
                            if op2 == "1":
                                main()
                            elif op2 == "2":
                                break
                            else:
                                print("Carácter inválido!")
                if op2 == "2":
                    break

                elif letra not in palavraChave:
                    erros = erros + 1
                    print("A palavra não tem essa letra.\n Erro:", erros)
                    if erros > 5:
                        vencedor = desafiante
                        perdedor = competidor
                        gravarArquivos()
                        while True:
                            print("Histórico de jogos:\n"+lerHistorico)
                            print(competidor+", você perdeu!")
                            print("O que você deseja fazer?")
                            print("(1) Jogar novamente")
                            print("(2) Sair")
                            op2 = input()
                            os.system("cls")
                            if op2 == "1":
                                main()
                            elif op2 == "2":
                                break
                            else:
                                print("Carácter inválido!")
                    if op2 == "2":
                        break
                       
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
                                print("O que você deseja fazer?")
                                print("(1) Jogar novamente")
                                print("(2) Sair")
                                op2 = input()
                                os.system("cls")
                                if op2 == "1":
                                    main()
                                elif op2 == "2":
                                    break
                                else:
                                    print("Carácter inválido!")
                    if op2 == "2":
                        break

                    elif letra not in palavraChave:
                        erros = erros + 1
                        print("A palavra não tem essa letra.\n Erro:", erros)
                        if erros > 5:
                            vencedor = desafiante
                            perdedor = competidor
                            gravarArquivos()
                            while True:
                                print("Histórico de jogos:\n"+lerHistorico)
                                print(competidor+", você perdeu!")
                                print("O que você deseja fazer?")
                                print("(1) Jogar novamente")
                                print("(2) Sair")
                                op2 = input()
                                os.system("cls")
                                if op2 == "1":
                                    main()
                                elif op2 == "2":
                                    break
                                else:
                                    print("Carácter inválido!")   
                        if op2 == "2":
                            break                     
            
        elif op == "2":
            if dicasCont > 2:
                print("Você não tem mais dicas!")
            else:
                print(dicas[dicasCont])
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
                                print(competidor+", você ganhou!")
                                print("O que você deseja fazer?")
                                print("(1) Jogar novamente")
                                print("(2) Sair")
                                op2 = input()
                                os.system("cls")
                                if op2 == "1":
                                    main()
                                elif op2 == "2":
                                    break
                                else:
                                    print("Carácter inválido!") 
                    if op2 == "2":
                        break
                                           

                    elif letra not in palavraChave:
                        erros = erros + 1
                        print("A palavra não tem essa letra.\n Erro:", erros)
                        if erros > 5:
                            vencedor = desafiante
                            perdedor = competidor
                            gravarArquivos()
                            while True:
                                print("Histórico de jogos:\n"+lerHistorico)
                                print(competidor+", você perdeu!")
                                print("O que você deseja fazer?")
                                print("(1) Jogar novamente")
                                print("(2) Sair")
                                op2 = input()
                                os.system("cls")
                                if op2 == "1":
                                    main()
                                elif op2 == "2":
                                    break
                                else:
                                    print("Carácter inválido!")
                        if op2 == "2":
                            break

        elif op == "3":
            break

        else:
            print("Caracter inválido!")

main()