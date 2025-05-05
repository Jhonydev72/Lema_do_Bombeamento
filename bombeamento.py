def lema_do_bombeamento(funcao_da_linguagem, p, w):
    '''Função que verifica se a liguagem é regular ou não, através do lema de bombeamento
    
        A função recebe como parametro a função da linguagem a ser testada, o numero de bombeamento e a cadeia 
         a ser testada '''

    n = len(w)  #tamanho da cadeia
    
    if n >= p: #verifica se o numero de bombeamento é maior ou igual ao tamanho da cadeia
        for i in range(1, p + 1):
            for j in range(1 ,i + 1):
                x = w[:j-1]
                y = w[j-1:i]
                z = w[i:]
                print(x, y, z)
                if len(y) == 0:
                    continue

                bombeamento = x + z
                if not funcao_da_linguagem(bombeamento):
                    print("divisão encontrada que quebra o lema: x='{}', y='{}', z='{}'" .format(x,y,z))
                    print("para i=0: '{}' não esta na linguagem" .format(bombeamento))
                    return 0
                
                bombeamento1 = x + y + z
                if not funcao_da_linguagem(bombeamento1):
                    print("divisão encontrada que quebra o lema: x='{}', y='{}', z='{}'" .format(x,y,z))
                    print("para i=1: '{}' não esta na linguagem" .format(bombeamento1))
                    return 0
                
                bombeamento2 = x + y * 2 + z
                if not funcao_da_linguagem(bombeamento2):
                    print("divisão encontrada que quebra o lema: x='{}', y='{}', z='{}'" .format(x,y,z))
                    print("para i=2: '{}' não esta na linguagem" .format(bombeamento2))
                    return 0
                
                bombeamento3 = x + y * 3 + z
                if not funcao_da_linguagem(bombeamento3):
                    print("divisão encontrada que quebra o lema: x='{}', y='{}', z='{}'" .format(x,y,z))
                    print("para i=3: '{}' não esta na linguagem" .format(bombeamento3))
                    return 0
    

        print("Nenhuma divisão quebra o lema - a linguagem pode ser regular")
        return 1

    else:
        print("a cadeia {} deve ser maior ou  igual ao valor de p = {}" .format(w, p))
        return 2
        




def linguagem_an_bn(cadeia):

    contagem_a = 0
    contagem_b = 0
    visto_b = False

    for caractere in cadeia:
        if caractere == 'a':
            if visto_b:
                return False
            contagem_a += 1
        elif caractere == 'b':
            visto_b = True
            contagem_b += 1
        else:
            False
    return contagem_a == contagem_b

p = 4.9
w = "aaaabbbb"

resultado = lema_do_bombeamento(linguagem_an_bn, p, w)
if resultado == 0:
    print("A linguagem não é regular (o lema foi quebrado)")
elif resultado == 1:
    print("O teste não encontrou contradição")
 

