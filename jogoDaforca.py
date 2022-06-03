# fazer print para mostrar letras digitadas
# ver erro linha 63 no segundo loop
# controlar a quantidade de erros em que o jogo termina (6)


import os

digitadas = []
erros = 0

desafiante = str(input("Desafiante: "))
competidor = str(input("Competidor: "))
os.system("cls")

print(desafiante,", responda as perguntas a seguir.\n ATENÇÂO! Não deixe que o competidor veja.")
palavraChave = str(input("Digite uma palavra-chave: "))
estadoAtual = ["*" for _ in range(len(palavraChave))]
dica1 = str(input("Digite a primeira dica: "))
dica2 = str(input("Digite a segunda dica: "))
dica3 = str(input("Digite a terceira dica: "))
dicas = [dica1, dica2, dica3]
os.system("cls")
dicasCont = 0
while True:
    print ("A palavra contém",len(palavraChave),"letras.\n",estadoAtual)
    print(competidor,", o que você deseja fazer?\n")
    print("(1) Jogar")
    print("(2) Solicitar Dica")
    op = input()
    if op == "1":
        letra = input("Digite uma letra.\n")
        digitadas.append(letra)
        if len(letra) == 1:
            os.system("cls")
            if letra in palavraChave:
                for i in range(len(palavraChave)):
                    if letra == palavraChave[i]:
                        estadoAtual[i] = letra
                print("Você acertou a letra!")
            elif letra not in palavraChave:
                erros = erros + 1
                print("A palavra não tem essa letra.\n Erro:", erros)
                if erros >= 6:
                    print("Você perdeu!")
        else:
            print("ERRO! Só é permitido digitar uma letra.")
            letra = input("Digite uma letra.")
            digitadas.append(letra)
            if len(letra) == 1:
                os.system("cls")
                if letra in palavraChave:
                    for i in range(len(palavraChave)):
                        if letra == palavraChave[i]:
                            estadoAtual[i] = letra
                    print("Você acertou a letra!")
                elif letra not in palavraChave:
                    erros = erros + 1
                    print("A palavra não tem essa letra.\n Erro:", erros)
                    if erros >= 6:
                        print("Você perdeu!")      
    
    elif op == "2":
        if dicasCont> 2:
            print("vc nao tem mais dicas")
        else:
            print(dicas[dicasCont])
            dicasCont = dicasCont + 1
        #dicas = dicas.remove(dicas[0]) 

        letra = input("Digite uma letra.\n")
        digitadas.append(letra)

        if len(letra) == 1:
            os.system("cls")
            if letra in palavraChave:
                for i in range(len(palavraChave)):
                    if letra == palavraChave[i]:
                        estadoAtual[i] = letra
                print("Você acertou a letra!")
            elif letra not in palavraChave:
                erros = erros + 1
                print("A palavra não tem essa letra.\n Erro:", erros)
                if erros >= 6:
                    print("Você perdeu!")     
    else:
        print("Caracter inválido!")
