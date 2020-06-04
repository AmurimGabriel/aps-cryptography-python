import random as rd
import sys
import os.path
import time

def fCriptografar(texto):
    
    textoInteiro = [bin(ord(letra))[2:] for letra in texto]
	
    textoBinario=""
    
    for integer in textoInteiro:
        while len(integer)!=8:
            integer = "0"+integer
	    
        textoBinario = textoBinario+integer
        
    chaves = geradorChave(int(len(textoBinario)/2), 16)

    cifra = cifrar(textoBinario, chaves)

    chaves.append(cifra)
    
    return chaves

def fDescriptografar(cifraTexto, chavesTexto):
    
    chavesTexto.reverse()

    textoCifrado = cifrar(cifraTexto, chavesTexto)
    
    resultadoChar = [chr(int(textoCifrado[i:i+8], 2)) for i in range(0, len(textoCifrado),8)]
    
    textoFinal=""

    for i in resultadoChar:
        textoFinal = textoFinal+i
    
    return textoFinal

def cifrar(texto, chaves):    
    
    for chave in chaves:
        L, R = texto[:int(len(texto)/2)], texto[int(len(texto)/2):]
        Ln = xor(L, xor(chave, R))
        texto = R + Ln
        
    return Ln + R

def xor(a, b):
      
    saida=""
    for i in range(len(a)):
        inter=int(a[i])+int(b[i])
        if inter==2: inter=0
        saida = saida+str(inter)
    return saida

def geradorChave(l,n):
    o=[]
    for i in range(n):
        k=""
        for i in range(l):
            k = k + str(rd.randint(0,1))
        o.append(k)
    return o

def verificadorCampo(texto):

    ok =  True
    if(texto != ""):
        for i in texto:
            if(i == " "):
                ok = False
            else:
                ok = True
                break
    else:
        ok =  False
    return ok


print("  ========================================================================")
print("||                                                                        ||")
print("||                      APS - REDE DE FEISTEL                             ||")
print("||                                                  by APS F.O.D.A        ||")
print("  ========================================================================")

login = ""
senha = ""

escolhaA = "S"
escolhaB = ""
tipoUsuario = ""

arquivoChaves = []
arquivoSenha = ""

print("")
print("Bem vindo/a !!")
print("")

while(True):
    print("Entre com o usuário. Se o usuário ainda não existir criaremos um para você! \n")

    while(True):

        
        login = input("Usuário: ")
        
        if(verificadorCampo(login)):
            
            if(not os.path.exists("user" + login + ".txt")):
                print("Usuário não cadastrado! \n")

                while(True):
                    print("Deseja cadastrar o usuário '" , login , "'? (S) / (N)")
                    cadastrar = input("Opção: ").upper()
                    print("")
                    if(cadastrar == "S"):
                        tipoUsuario = "A"
                        break
                    elif(cadastrar == "N"):
                        tipoUsuario = ""
                        break
                    else:
                        print("Por favor, digite uma opção válida! \n")
            else:
                tipoUsuario = "B"
        else:
            print("Login inválido. É necessário ao menos um caracter! \n")
  

        if(tipoUsuario == "A"):
            print("Criação de novo usuário;")
            while(True):
                senha = input("Senha: ")
                if(verificadorCampo(senha)):
                    senhaConfi = input("Confirmação de senha: ")
                    print("")

                    if(senha == senhaConfi):
                        
                        chaves = fCriptografar(senha)
                        
                        arquivo = open("user" + login + ".txt", 'w')

                        for chave in chaves:
                            arquivo.write(chave + "\n")

                        arquivo.close()

                        print("Sua senha cifrado foi salvo no arquivo 'user" + login + ".txt'. \nPor favor, guarde este arquivo pois ele será "+
                              "necessário para o próximo acesso.\n")
                        break
                    else:
                        print("Confirmação de senha não corresponde! Digite a senha novamente; \n")
                else:
                    print("Senha inválida. É necessário ao menos um caracter!")
                
            break       

        if(tipoUsuario == "B"):

            print("Usuário já existente! Entre com a senha. \n")

            senha = input("Senha: ")
            print("")

            arquivoLogin = open("user" + login + ".txt", 'r')

            arquivoChaves = []
            arquivoSenha = ""
            
            for linha in arquivoLogin:
                arquivoChaves.append(linha[:-1])
            
            for linha in arquivoChaves:
                arquivoSenha = linha

            del arquivoChaves[-1]

            senhaDecifrada = fDescriptografar(arquivoSenha, arquivoChaves)
            
            if(senha == senhaDecifrada):
                break
            else:
                print("Senha incorreta!! Digite Usuário e Senha novamente. \n")

    while(escolhaA == "S"):
        print("  ==============================")
        print("||                              ||")
        print("||    Escolha uma opção :       ||")
        print("||                              ||")
        print("||       Cifrar   (A)           ||")
        print("||       Decifrar (B)           ||")
        print("||       Trocar                 ||")
        print("||       Usuário  (C)           ||")
        print("||       Sair     (X)           ||")
        print("||                              ||")    
        print("  ==============================")   

        escolhaB = input("Opção: ").upper()
        print("")

        if(escolhaB == "A"):

            cifra = ""
            arquivo = ""
            texto = ""
            
            print("Cifragem de texto; \n")
            
            while(True):
                texto = input("Texto a ser cifrado: ")
                         
                if(verificadorCampo(texto)):
                    chaves = fCriptografar(texto)

                    nomeArquivo = ""                
                    while(True):

                        nomeArquivo = input("Escolha um nome para seu arquivo de texto: ")
                        print("")

                        if(not os.path.exists(nomeArquivo + ".txt")):
                            arquivo = open(nomeArquivo + ".txt", 'w')

                            for chave in chaves:
                                arquivo.write("%s\n" % chave)

                            print("")
                            print("CRIPTOGRAFANDO ARQUIVO...")
                            time.sleep(2)
                            print("[*****   35%       ]")
                            time.sleep(2)
                            print("[********78%****   ]")
                            time.sleep(1)
                            print("[********99%*******]")
                            time.sleep(1)            
                            print("")
                            
                            print("Seu texto cifrado foi salvo no arquivo '" + nomeArquivo + ".txt'.\n Por favor, guarde este arquivo pois ele será "+
                                  "necessário para decifrar o texto.\n")

                            arquivo.close()
                            print("RETORNANDO PARA O MENU... \n")
                            time.sleep(1)
                            break
                        else:
                            print("Um arquivo com este nome já existe! Por favor, digite um nome diferente; \n")
                            print("Texto a ser cifrado: " , texto)
                    break
                else:
                    print("Texto inválido! É necessário ao menos um caracteres! \n")
    
                
        elif(escolhaB == "B"):
            print("Decifrar arquivo;\n")
            
            arquivo = ""
            
            while(True):
                arquivoNome = input("Nome do arquivo .txt: ")            

                if(not os.path.exists(arquivoNome + ".txt")):
                    print("Arquivo não encontrado!! Digite novamente.\n")

                else:
                    arquivo = open(arquivoNome + ".txt", 'r')
                    
                    arquivoLido = []
                    cifra = ""
                    
                    for linha in arquivo:
                        arquivoLido.append(linha[:-1])

                    del arquivoLido[-1]
                
                    arquivoDois = open(arquivoNome + ".txt", 'r')

                    for linha in arquivoDois:
                        cifra = linha[:-1]

                    print("")
                    print("ACESSANDO ARQUIVO...")
                    time.sleep(2)
                    print("CONVERTENDO PALAVRAS...")
                    time.sleep(2)
                    print("[*****   35%       ]")
                    time.sleep(2)
                    print("[********78%****   ]")
                    time.sleep(2)
                    print("[********99%*******]")
                    time.sleep(1)
                    print("ARQUIVO CONVERTIDO COM SUCESSO!!\n")
                    
                    print("O resultado da decifração do texto é: ")
                    print("")
                    print("  " + fDescriptografar(cifra, arquivoLido))
                    print("")
                    
                    arquivo.close()
                    arquivoDois.close()

                    print("RETORNANDO PARA O MENU... \n")
                    time.sleep(1)
                    break


        elif(escolhaB == "X"):
            print("Volte sempre! ;)")
            sys.exit()
        elif(escolhaB == "C"):
            print("RETORNANDO PARA O LOGIN... \n")
            time.sleep(1)
            break

        else:
            print("Por favor, digite uma opção válida!!")
            

