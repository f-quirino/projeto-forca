import random

def sortear_palavra():
    pasta = 'C:\\Users\\Flávio Quirino\\Desktop\\Programação\\Curso Lets Code - Pi DS\Projetos\\Logica de Programação e POO\\Jogo da forca\\'
    arquivo = open(pasta + 'animais.txt','r',encoding='utf-8')
    lista_animais = arquivo.read().split(',')
    arquivo.close()

    palavra_secreta = random.choices(lista_animais)
    return palavra_secreta[0]


#def sortear_palavra():
#    lista_palavra = ['abelha', 'andorinha', 'babuino', 'baleia', 'cachorro', 'camaleao', 
#                    'elefante', 'foca', 'flamingo', 'golfinho', 'guaxinim', 'hiena', 'iguana',
#                    'jaguar', 'jacare', 'leao', 'lagarto', 'macaco', 'ovelha', 'orangotango', 
#                    'papagaio', 'raposa', 'rato', 'sardinha', 'sagui', 'tartaruga', 'urubu', 
#                    'veado', 'vaca', 'zebra']
#    palavra_secreta = random.choices(lista_palavra)
#    return palavra_secreta[0]


def ocultar(palavra):
    word = ['_' for letra in palavra]
    return word
    
# def ocultar(palavra):
#    word = []
#    for letra in palavra:
#        letra = '_'
#        word.append(letra)
#    return word

def pedir_letra():
    letra = input('Escolha uma letra: ').lower()
    return letra

def letra_correta(pedir_letra, dica, palavra_secreta):
    for idx, letra in enumerate(palavra_secreta):
        if pedir_letra == letra:
            dica[idx] = pedir_letra
    print(dica)

def letras_digitadas(letra, repitidas):
    if letra in repitidas:
        print('Letra já digitada, escolha outra letra!!')
    else:
        repitidas.append(letra)
    return repitidas

def desenho(erros):
    
    if erros == 0:
        print("  _______       ")
        print(" |       |      ")
        print(" |              ")
        print(" |          \O/ ")
        print(" |           |  ")
        print(" |          / \ ")
        print(" |XXXXXXXXXXXXXX\n")
        
    elif erros == 1:
        print("  _______       ")
        print(" |       |      ")
        print(" |       O      ")
        print(" |              ")
        print(" |              ")
        print(" |              ")
        print(" |XXXXXXXXXXXXXX\n")
        
    elif erros == 2:
        print("  _______       ")
        print(" |       |      ")
        print(" |       O      ")
        print(" |       |      ")
        print(" |              ")
        print(" |              ")
        print(" |XXXXXXXXXXXXXX\n")
               
    elif erros == 3:
        print("  _______       ")
        print(" |       |      ")
        print(" |       O      ")
        print(" |      /|      ")
        print(" |              ")
        print(" |              ")
        print(" |XXXXXXXXXXXXXX\n")
        
    elif erros == 4:
        print("  _______       ")
        print(" |       |      ")
        print(" |       O      ")
        print(" |      /|\     ")
        print(" |              ")
        print(" |              ")
        print(" |XXXXXXXXXXXXXX\n")
         
    elif erros == 5:
        print("  _______       ")
        print(" |       |      ")
        print(" |       O      ")
        print(" |      /|\     ")
        print(" |      /       ")
        print(" |              ")
        print(" |XXXXXXXXXXXXXX\n")
    else:
        print("  _______       ")
        print(" |       |      ")
        print(" |       O      ")
        print(" |      /|\     ")
        print(" |      / \     ")
        print(" |              ")
        print(" |XXXXXXXXXXXXXX\n")


def play():
    
    print('xxx JOGO DA FORCA xxx\n  x Tema Animais x\n')

    letras_usadas = []
    palavra_secreta = sortear_palavra()
    dica = ocultar(palavra_secreta)
    print(dica)
    erros = 0

    while (('_' in dica) and (erros != 6)):
        letra = pedir_letra()
        letras_usadas = letras_digitadas(letra, letras_usadas)
        print(f'\nLetras usadas: {letras_usadas}\n' )

        if letra in palavra_secreta:
            letra_correta(letra, dica, palavra_secreta)
            if '_' not in dica:
                print() 
                print('*'*20)         
                print('*** Você ganhou! ***')
                print('*'*20,'\n')    
                if erros == 0:
                    desenho(0)
                
        else:
            erros += 1
            print(dica)
            print('\nVocê ainda tem {} vidas\n'.format(6-erros))
            desenho(erros)
            if erros == 6:
                print(f'\nA paravra era {palavra_secreta}.\n')
                print('*'*20)
                print('*** Você perdeu! ***')
                print('*'*20)
play()