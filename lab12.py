# lab12 by heusmat
from recipes_decimal import pi
from decimal import getcontext, Decimal
getcontext().prec = 36
pi = pi()


def funcao_distancia(a, b, c, d, x):
    '''Dados os parâmetros a, b, c, d e a variável x, calcula a distância em
    anos-luz que a espaço-moto pode percorrer com uma quantidade x de
    combustível em seu tanque (em hawkins)'''

    valor_de_zeta = zeta(b, x)
    e_elevado_a_raiz = Decimal(- (Decimal(c * x).sqrt())).exp()
    numerador = (pi + a * Decimal(x).exp() - valor_de_zeta)
    denominador = e_elevado_a_raiz + d * (Decimal(2) * pi ** Decimal(3) - x)
    return numerador / denominador


def zeta(b, x):
    '''Retorna o somatório de zeta: 1 / n^s, com n variando de 1 a 100.
    Necessário para a função distância'''

    somatorio = 0
    const_s = b * x + pi
    for n in range(1, 101):
        soma_parcial = Decimal(1) / (Decimal(n) ** const_s)
        somatorio += soma_parcial
    return somatorio


def filtrar_planetas(dist_max, dic_planetas_dists):
    '''Dividida em duas partes: a primeira cria um novo dicionário que
    contém apenas os planetas dentro da distância máxima possível
    de ser percorrida pelo robô. A segunda parte seleciona o planeta com a
    maior distância dentre as possíveis, e o retorna em tupla junto de sua
    distância em anos-luz'''

    novo_dic = {}
    for i in dic_planetas_dists:  # Parte 1 - planetas dentro do intervalo
        if dic_planetas_dists[i] < dist_max:
            novo_dic[i] = dic_planetas_dists[i]
    if len(novo_dic) == 0:
        return 'GRAU~~'
    planeta_escolhido = ' '
    distancia_escolhida = 0
    for j in novo_dic:  # Parte 2 - planeta mais distante
        if novo_dic[j] > distancia_escolhida:
            distancia_escolhida = novo_dic[j]
            planeta_escolhido = j
    return (planeta_escolhido, distancia_escolhida)


def busca_antimateria(a, b, c, d, distancia_real):
    '''Função de busca binária. Esta função encontra o valor de x
    (combustível em hawkins) para percorrer uma determinada distância
    y (distancia_real - em anos-luz até o planeta escolhido).
    Para tanto, faz tentativa e erro, substituindo x na funcao_
    distancia.'''

    erro = Decimal(10) ** Decimal(-32)
    esquerda = Decimal(0)
    direita = Decimal(50)
    while abs(esquerda - direita) > erro:
        x = (esquerda + direita) / 2
        distancia_atual = funcao_distancia(a, b, c, d, x)
        if distancia_real > distancia_atual:
            esquerda = x
        else:
            direita = x
    return x


def main():
    '''Código principal. Abrange as entradas e as demais funções.
    Também realiza a impressão do planeta mais distante possível e
    do combustível necessário para ir até ele.'''

    dic_planetas_dists = {}
    qtd_rotas = int(input())
    while qtd_rotas != 0:
        dic_planetas_dists = {}
        for i in range(qtd_rotas):
            nome_do_planeta = input()
            distancia_em_anos_luz = Decimal(input())
            dic_planetas_dists[nome_do_planeta] = distancia_em_anos_luz
        parametro_a = Decimal(input())
        parametro_b = Decimal(input())
        parametro_c = Decimal(input())
        parametro_d = Decimal(input())
        dist_max = funcao_distancia(parametro_a, parametro_b, parametro_c,
                                    parametro_d, Decimal(50))
        planeta_escolhido_e_dist = filtrar_planetas(dist_max,
                                                    dic_planetas_dists)
        if planeta_escolhido_e_dist != 'GRAU~~':
            qtd_antimateria = busca_antimateria(parametro_a, parametro_b, parametro_c, 
                                                parametro_d, planeta_escolhido_e_dist[1])
            print(planeta_escolhido_e_dist[0])
            print(f'{qtd_antimateria:.28f}')
        else:
            print('GRAU~~')
        qtd_rotas = int(input())


if __name__ == '__main__':
    main()
