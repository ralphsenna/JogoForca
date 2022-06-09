import random
ani_faci=['COBRA', 'LEÃO', 'GATO']
ani_difi=['LEOPARDO', 'GOLFINHO', 'HIPOPÓTAMO']
fruta_faci=['MAÇA', 'PERA', 'UVA']
fruta_difi=['PITANGA', 'CARAMBOLA', 'KIWI']
marca_faci=['INTEL', 'NIKE', 'SONY']
marca_difi=['LOUIS VUITTON', 'FORTREK', 'HOLLISTER']
nome_faci=['RAFAEL', 'JOÃO', 'VITOR']
nome_difi=['BENJAMIN', 'AURORA', 'OSWALDO']
forca=["""   +----+
    |    |
         |
         |
         |
         |""","""   +----+
    |    |
    O    |
         |
         |
         |""","""   +----+
    |    |
    O    |
    |    |
         |
         |""","""   +----+
    |    |
    O    |
   /|    |
         |
         |""","""   +----+
    |    |
    O    |
   /|\   |
         |
         |""","""   +----+
    |    |
    O    |
   /|\   |
   /     |
         |""","""   +----+
    |    |
    O    |
   /|\   |
   / \   |
         |"""]
print("         |---  Jogo da Forca  ---|")
print("""    +----+
    |    |
    O    |
   /|\   |
   / \   |
         |
=============\n""")
resp=input("Vamos Jogar? (Use 'S' para Sim e 'N' para Não)\n")
while (resp=='S'):
    difi=int(input("""      --Dificuldades--
  1 - Fácil
  2 - Difícil
Dificuldade: """))
    if (difi==1):
        cate=int(input("""\n    --Categorias--
  1 - Animais
  2 - Frutas
  3 - Marcas
  4 - Nomes 
Categoria: """))
        print("")
        palavra_desconhecida=[]
        letras_erradas=[]
        if (cate==1):
            palavra=random.choice(ani_faci)
            print(letras_erradas)
            print("", forca[0])
            num=len(palavra)
            for i in range(num):
                palavra_desconhecida.append("_")
            for i in range(num):
                print(" ", palavra_desconhecida[i])
            lista_palavra=palavra
            chances=0
            cont=0
            while (chances!=6 and cont!=num):
                letra=input("Informe uma letra: ")
                print("")
                letra=letra.upper()
                achou=0
                for i in range(num):
                    if letra==lista_palavra[i]:
                        palavra_desconhecida[i]=letra
                        achou+=1
                        cont+=1
                if (achou==0):
                    chances+=1
                    letras_erradas.append(letra)
                if (chances==3):
                    ajuda=input("Precisa de uma ajuda? (Use 'S' para Sim e 'N' para Não)\n")
                    if (ajuda=='S'):
                        vez=0
                        for i in range(num):
                            if palavra_desconhecida[i]=='_' and vez==0:
                                palavra_desconhecida[i]=lista_palavra[i]
                                cont+=1
                                vez+=1
                                chances+=1
                print(letras_erradas)
                print("", forca[chances])
                for i in range(num):
                    print(" ", palavra_desconhecida[i])
            if cont==num:
                print("\nPárabens, você acertou a palavra!")
                resp=input("\nGostaria de jogar novamente? (Use 'S' para Sim e 'N' para Não)\n")
            else:
                print("\nVocê não conseguiu descobrir a palavra :(\nA palavra era:", palavra)
                resp = input("\nGostaria de jogar novamente? (Use 'S' para Sim e 'N' para Não)\n")
        elif (cate==2):
            palavra = random.choice(fruta_faci)
            print(letras_erradas)
            print("", forca[0])
            num = len(palavra)
            for i in range(num):
                palavra_desconhecida.append("_")
            for i in range(num):
                print(" ", palavra_desconhecida[i])
            lista_palavra = palavra
            chances = 0
            cont = 0
            while (chances != 6 and cont != num):
                letra = input("Informe uma letra: ")
                print("")
                letra = letra.upper()
                achou = 0
                for i in range(num):
                    if letra == lista_palavra[i]:
                        palavra_desconhecida[i] = letra
                        achou += 1
                        cont += 1
                if (achou == 0):
                    chances += 1
                    letras_erradas.append(letra)
                if (chances == 3):
                    ajuda = input("Precisa de uma ajuda? (Use 'S' para Sim e 'N' para Não)\n")
                    if (ajuda == 'S'):
                        vez = 0
                        for i in range(num):
                            if palavra_desconhecida[i] == '_' and vez == 0:
                                palavra_desconhecida[i] = lista_palavra[i]
                                cont += 1
                                vez += 1
                                chances += 1
                print(letras_erradas)
                print("", forca[chances])
                for i in range(num):
                    print(" ", palavra_desconhecida[i])
            if cont == num:
                print("\nPárabens, você acertou a palavra!")
                resp = input("\nGostaria de jogar novamente? (Use 'S' para Sim e 'N' para Não)\n")
            else:
                print("\nVocê não conseguiu descobrir a palavra :(\nA palavra era:", palavra)
                resp = input("\nGostaria de jogar novamente? (Use 'S' para Sim e 'N' para Não)\n")
        elif (cate==3):
            palavra = random.choice(marca_faci)
            print(letras_erradas)
            print("", forca[0])
            num = len(palavra)
            for i in range(num):
                palavra_desconhecida.append("_")
            for i in range(num):
                print(" ", palavra_desconhecida[i])
            lista_palavra = palavra
            chances = 0
            cont = 0
            while (chances != 6 and cont != num):
                letra = input("Informe uma letra: ")
                print("")
                letra = letra.upper()
                achou = 0
                for i in range(num):
                    if letra == lista_palavra[i]:
                        palavra_desconhecida[i] = letra
                        achou += 1
                        cont += 1
                if (achou == 0):
                    chances += 1
                    letras_erradas.append(letra)
                if (chances == 3):
                    ajuda = input("Precisa de uma ajuda? (Use 'S' para Sim e 'N' para Não)\n")
                    if (ajuda == 'S'):
                        vez = 0
                        for i in range(num):
                            if palavra_desconhecida[i] == '_' and vez == 0:
                                palavra_desconhecida[i] = lista_palavra[i]
                                cont += 1
                                vez += 1
                                chances += 1
                print(letras_erradas)
                print("", forca[chances])
                for i in range(num):
                    print(" ", palavra_desconhecida[i])
            if cont == num:
                print("\nPárabens, você acertou a palavra!")
                resp = input("\nGostaria de jogar novamente? (Use 'S' para Sim e 'N' para Não)\n")
            else:
                print("\nVocê não conseguiu descobrir a palavra :(\nA palavra era:", palavra)
                resp = input("\nGostaria de jogar novamente? (Use 'S' para Sim e 'N' para Não)\n")
        elif (cate==4):
            palavra = random.choice(nome_faci)
            print(letras_erradas)
            print("", forca[0])
            num = len(palavra)
            for i in range(num):
                palavra_desconhecida.append("_")
            for i in range(num):
                print(" ", palavra_desconhecida[i])
            lista_palavra = palavra
            chances = 0
            cont = 0
            while (chances != 6 and cont != num):
                letra = input("Informe uma letra: ")
                print("")
                letra = letra.upper()
                achou = 0
                for i in range(num):
                    if letra == lista_palavra[i]:
                        palavra_desconhecida[i] = letra
                        achou += 1
                        cont += 1
                if (achou == 0):
                    chances += 1
                    letras_erradas.append(letra)
                if (chances == 3):
                    ajuda = input("Precisa de uma ajuda? (Use 'S' para Sim e 'N' para Não)\n")
                    if (ajuda == 'S'):
                        vez = 0
                        for i in range(num):
                            if palavra_desconhecida[i] == '_' and vez == 0:
                                palavra_desconhecida[i] = lista_palavra[i]
                                cont += 1
                                vez += 1
                                chances += 1
                print(letras_erradas)
                print("", forca[chances])
                for i in range(num):
                    print(" ", palavra_desconhecida[i])
            if cont == num:
                print("\nPárabens, você acertou a palavra!")
                resp = input("\nGostaria de jogar novamente? (Use 'S' para Sim e 'N' para Não)\n")
            else:
                print("\nVocê não conseguiu descobrir a palavra :(\nA palavra era:", palavra)
                resp = input("\nGostaria de jogar novamente? (Use 'S' para Sim e 'N' para Não)\n")
    elif (difi==2):
        cate=int(input("""\n    --Categorias--
          1 - Animais
          2 - Frutas
          3 - Marcas
          4 - Nomes
Categoria: """))
        print("")
        palavra_desconhecida = []
        letras_erradas = []
        if (cate == 1):
            palavra = random.choice(ani_difi)
            print(letras_erradas)
            print("", forca[0])
            num = len(palavra)
            for i in range(num):
                palavra_desconhecida.append("_")
            for i in range(num):
                print(" ", palavra_desconhecida[i])
            lista_palavra = palavra
            chances = 0
            cont = 0
            while (chances != 6 and cont != num):
                letra = input("Informe uma letra: ")
                print("")
                letra = letra.upper()
                achou = 0
                for i in range(num):
                    if letra == lista_palavra[i]:
                        palavra_desconhecida[i] = letra
                        achou += 1
                        cont += 1
                if (achou == 0):
                    chances += 1
                    letras_erradas.append(letra)
                if (chances == 3):
                    ajuda = input("Precisa de uma ajuda? (Use 'S' para Sim e 'N' para Não)\n")
                    if (ajuda == 'S'):
                        vez = 0
                        for i in range(num):
                            if palavra_desconhecida[i] == '_' and vez == 0:
                                palavra_desconhecida[i] = lista_palavra[i]
                                cont += 1
                                vez += 1
                                chances += 1
                print(letras_erradas)
                print("", forca[chances])
                for i in range(num):
                    print(" ", palavra_desconhecida[i])
            if cont == num:
                print("\nPárabens, você acertou a palavra!")
                resp = input("\nGostaria de jogar novamente? (Use 'S' para Sim e 'N' para Não)\n")
            else:
                print("\nVocê não conseguiu descobrir a palavra :(\nA palavra era:", palavra)
                resp = input("\nGostaria de jogar novamente? (Use 'S' para Sim e 'N' para Não)\n")
        elif (cate == 2):
            palavra = random.choice(fruta_difi)
            print(letras_erradas)
            print("", forca[0])
            num = len(palavra)
            for i in range(num):
                palavra_desconhecida.append("_")
            for i in range(num):
                print(" ", palavra_desconhecida[i])
            lista_palavra = palavra
            chances = 0
            cont = 0
            while (chances != 6 and cont != num):
                letra = input("Informe uma letra: ")
                print("")
                letra = letra.upper()
                achou = 0
                for i in range(num):
                    if letra == lista_palavra[i]:
                        palavra_desconhecida[i] = letra
                        achou += 1
                        cont += 1
                if (achou == 0):
                    chances += 1
                    letras_erradas.append(letra)
                if (chances == 3):
                    ajuda = input("Precisa de uma ajuda? (Use 'S' para Sim e 'N' para Não)\n")
                    if (ajuda == 'S'):
                        vez = 0
                        for i in range(num):
                            if palavra_desconhecida[i] == '_' and vez == 0:
                                palavra_desconhecida[i] = lista_palavra[i]
                                cont += 1
                                vez += 1
                                chances += 1
                print(letras_erradas)
                print("", forca[chances])
                for i in range(num):
                    print(" ", palavra_desconhecida[i])
            if cont == num:
                print("\nPárabens, você acertou a palavra!")
                resp = input("\nGostaria de jogar novamente? (Use 'S' para Sim e 'N' para Não)\n")
            else:
                print("\nVocê não conseguiu descobrir a palavra :(\nA palavra era:", palavra)
                resp = input("\nGostaria de jogar novamente? (Use 'S' para Sim e 'N' para Não)\n")
        elif (cate == 3):
            palavra = random.choice(marca_difi)
            print(letras_erradas)
            print("", forca[0])
            num = len(palavra)
            for i in range(num):
                palavra_desconhecida.append("_")
            for i in range(num):
                print(" ", palavra_desconhecida[i])
            lista_palavra = palavra
            chances = 0
            cont = 0
            while (chances != 6 and cont != num):
                letra = input("Informe uma letra: ")
                print("")
                letra = letra.upper()
                achou = 0
                for i in range(num):
                    if letra == lista_palavra[i]:
                        palavra_desconhecida[i] = letra
                        achou += 1
                        cont += 1
                if (achou == 0):
                    chances += 1
                    letras_erradas.append(letra)
                if (chances == 3):
                    ajuda = input("Precisa de uma ajuda? (Use 'S' para Sim e 'N' para Não)\n")
                    if (ajuda == 'S'):
                        vez = 0
                        for i in range(num):
                            if palavra_desconhecida[i] == '_' and vez == 0:
                                palavra_desconhecida[i] = lista_palavra[i]
                                cont += 1
                                vez += 1
                                chances += 1
                print(letras_erradas)
                print("", forca[chances])
                for i in range(num):
                    print(" ", palavra_desconhecida[i])
            if cont == num:
                print("\nPárabens, você acertou a palavra!")
                resp = input("\nGostaria de jogar novamente? (Use 'S' para Sim e 'N' para Não)\n")
            else:
                print("\nVocê não conseguiu descobrir a palavra :(\nA palavra era:", palavra)
                resp = input("\nGostaria de jogar novamente? (Use 'S' para Sim e 'N' para Não)\n")
        elif (cate == 4):
            palavra = random.choice(nome_difi)
            print(letras_erradas)
            print("", forca[0])
            num = len(palavra)
            for i in range(num):
                palavra_desconhecida.append("_")
            for i in range(num):
                print(" ", palavra_desconhecida[i])
            lista_palavra = palavra
            chances = 0
            cont = 0
            while (chances != 6 and cont != num):
                letra = input("Informe uma letra: ")
                print("")
                letra = letra.upper()
                achou = 0
                for i in range(num):
                    if letra == lista_palavra[i]:
                        palavra_desconhecida[i] = letra
                        achou += 1
                        cont += 1
                if (achou == 0):
                    chances += 1
                    letras_erradas.append(letra)
                if (chances == 3):
                    ajuda = input("Precisa de uma ajuda? (Use 'S' para Sim e 'N' para Não)\n")
                    if (ajuda == 'S'):
                        vez = 0
                        for i in range(num):
                            if palavra_desconhecida[i] == '_' and vez == 0:
                                palavra_desconhecida[i] = lista_palavra[i]
                                cont += 1
                                vez += 1
                                chances += 1
                print(letras_erradas)
                print("", forca[chances])
                for i in range(num):
                    print(" ", palavra_desconhecida[
                        i])
            if cont == num:
                print("\nPárabens, você acertou a palavra!")
                resp = input("\nGostaria de jogar novamente? (Use 'S' para Sim e 'N' para Não)\n")
            else:
                print("\nVocê não conseguiu descobrir a palavra :(\nA palavra era:", palavra)
                resp = input("\nGostaria de jogar novamente? (Use 'S' para Sim e 'N' para Não)\n")
print("Ok, até mais!")