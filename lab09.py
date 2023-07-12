# lab9 by heusmat
def criar_matriz(num_linhas):
    '''Cria a matriz ("imagem") principal, dada na entrada, e que será
    modificada pelas operações.'''

    matriz = []
    for i in range(num_linhas):
        linha_atual = input().split()
        matriz.append(linha_atual)
    return matriz


def selecionar_operacao():
    '''Escolha das operações, dadas pelas entradas: seleção, cópia, recorte ou
    espelhamento.Leva para outras funções de nomes análogos.'''

    global area_selecionada
    operacao = input().split()
    if operacao[0] == 'selecao':
        area_selecionada = mudar_coordenadas(int(operacao[1]), int(operacao[2]),
                                             int(operacao[3]), int(operacao[4]))
    elif operacao[0] == 'copia':
        op_copia(int(operacao[1]), int(operacao[2]))
    elif operacao[0] == 'recorte':
        op_recorte(int(operacao[1]), int(operacao[2]))
    elif operacao[0] == 'rotacao':
        op_rotacao()
    elif operacao[0] == 'espelhamento':
        op_espelhamento(operacao[1])


def mudar_coordenadas(op_1, op_2, op_3, op_4):
    '''Muda as coordenadas da seleção, para não confundir com as coordenadas das
    funções op_recorte e op_copia, onde a área selecionada será colada.'''

    global coord_x
    global coord_y
    global largura
    global altura
    coord_x = op_1
    coord_y = op_2
    largura = op_3
    altura = op_4
    return op_selecao()


def op_selecao():
    '''Seleciona e armazena na variável area_selecionada uma determinada parte da
    matriz, conforme os parâmetros dados na entrada e armazenados na função
    mudar_coordenadas.'''

    area_selecionada = []
    for i in range(coord_y, coord_y + altura):
        area_selecionada.append(matriz[i])
    for j in range(len(area_selecionada)):
        area_selecionada[j] = area_selecionada[j][coord_x:coord_x + largura]
    return area_selecionada


def op_copia(coord_cola_x, coord_cola_y):
    '''Copia e cola a área selecionada em um local da matriz principal especificado
    na entrada. A area_selecionada deve ser re-selecionada de acordo com os
    parâmetros anteriores pois, caso haja sobreposição, ela será alterada.'''

    global area_selecionada
    # Colando a área selecionada na matriz principal
    k = -1
    for i in range(coord_cola_y, coord_cola_y + altura):
        k += 1
        l = -1
        for j in range(coord_cola_x, coord_cola_x + largura):
            l += 1
            matriz[i][j] = area_selecionada[k][l]

    # E re-selecionando a área selecionada
    area_selecionada = op_selecao()


def op_recorte(coord_cola_x, coord_cola_y):
    '''Recorta e cola a área selecionada em um local da matriz principal
    especificado na entrada. A area_selecionada é zerada e, em seguida, deve
    ser re-selecionada de acordo com os parâmetros anteriores pois, caso haja
    sobreposição, ela será alterada.'''

    global area_selecionada
    # Primeiro, zerando a área recortada na matriz principal
    for i in range(coord_y, coord_y + altura):
        for j in range(coord_x, coord_x + largura):
            matriz[i][j] = '000'

    # Agora, colando a área selecionada na matriz principal
    k = -1
    for i in range(coord_cola_y, coord_cola_y + altura):
        k += 1
        l = -1
        for j in range(coord_cola_x, coord_cola_x + largura):
            l += 1
            matriz[i][j] = area_selecionada[k][l]

    # Por fim, re-selecionando a área selecionada
    area_selecionada = op_selecao()


def op_rotacao():
    '''Rotaciona a área selecionada em 90 graus no sentido horário,
    modificando a matriz principal no processo. Os píxeis não repostos são
    zerados. Ao fim, a area_selecionada é re-selecionada, pois se altera.'''

    global area_selecionada
    # 1- Zerando a área selecionada na matriz principal
    for i in range(coord_y, coord_y + altura):
        for j in range(coord_x, coord_x + largura):
            matriz[i][j] = '000'

    # 2- Criando uma matriz auxiliar, que é a área selecionada e rotacionada
    area_selecionada_rot = rotacionar_area()

    # 3- Colando a matriz rotacionada obtida na matriz principal
    k = -1
    for i in range(coord_y, coord_y + len(area_selecionada_rot)):
        k += 1
        l = -1
        for j in range(coord_x, coord_x + len(area_selecionada_rot[0])):
            l += 1
            matriz[i][j] = area_selecionada_rot[k][l]

    # 4- Re-selecionando a área selecionada anteriormente
    area_selecionada = op_selecao()


def rotacionar_area():
    '''Sub-função da operação de rotação. Gera uma nova matriz
    (area_selecionada_rot), que é a área selecionada rotacionada.
    Por fim, na função original, op_rotacao, esta nova matriz é colada na
    matriz principal.'''

    qtd_linhas_nova_matriz = largura
    nova_matriz = []
    l = -1
    for m in range(qtd_linhas_nova_matriz):
        nova_linha = []
        l += 1
        for n in range(altura - 1, -1, -1):
            nova_linha.append(area_selecionada[n][l])
        nova_matriz.append(nova_linha)
    return nova_matriz


def op_espelhamento(tipo):
    '''Dividida em duas partes: Horizontal e Vertical, que geram uma nova
    matriz espelhada a partir da area_selecionada. Essa nova matriz é, então,
    colada na matriz principal. Por fim, a área de seleção é re-selecionada, 
    pois se modificou.'''

    global area_selecionada
    if tipo == 'h':  # 1a- Espelhamento horizontal
        area_espelhada = []
        for i in range(len(area_selecionada)):
            nova_linha = []
            for j in range(len(area_selecionada[i])-1, -1, -1):
                nova_linha.append(area_selecionada[i][j])
            area_espelhada.append(nova_linha)

    if tipo == 'v':  # 1b- Espelhamento vertical
        area_espelhada = []
        for k in range(len(area_selecionada)-1, -1, -1):
            area_espelhada.append(area_selecionada[k])

    # 2- Colando a área espelhada na matriz principal
    k = -1
    for i in range(coord_y, coord_y + len(area_espelhada)):
        k += 1
        l = -1
        for j in range(coord_x, coord_x + len(area_espelhada[0])):
            l += 1
            matriz[i][j] = area_espelhada[k][l]

    # 3- Re-selecionando a área selecionada anteriormente
    area_selecionada = op_selecao()


def printar_matriz_final(matriz):
    '''Impressão da matriz principal após todas as modificações.'''
    for i in range(len(matriz)):
        linha_da_matriz = ' '.join(x for x in matriz[i])
        print(linha_da_matriz)


def main():
    '''Código principal.'''
    global matriz
    global area_selecionada
    area_selecionada = []
    colunasxlinhas = input().split()
    num_colunas = int(colunasxlinhas[0])
    num_linhas = int(colunasxlinhas[1])
    num_operacoes = int(input())
    matriz = criar_matriz(num_linhas)
    area_selecionada = mudar_coordenadas(0, 0, num_colunas, num_linhas)
    for i in range(num_operacoes):
        selecionar_operacao()
    printar_matriz_final(matriz)


if __name__ == '__main__':
    main()
