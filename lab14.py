# lab14 by heusmat - vacation_mode = True
def determinante_rec(matriz):
    '''Recebe uma matriz e calcula seu determinante, com base na Expansão
    de Laplace. É uma função recursiva, cujo caso-base é a matriz de dimensão
    2, pois seu cálculo é trivial.'''

    if len(matriz) == 2:
        return int(matriz[0][0]) * int(matriz[1][1]) - ((int(matriz[0][1]) * int(matriz[1][0])))
    else:
        soma_det = 0
        for i in range(len(matriz[0])):
            nova_matriz = remove_lin_col(matriz, i)
            det_atual = int(matriz[0][i]) * ((-1) ** i) * determinante_rec(nova_matriz)
            soma_det += det_atual
        return soma_det


def remove_lin_col(matriz, coluna):
    '''Devolve uma nova matriz sem a linha e a coluna do elemento da vez, como
    parte da Expansão de Laplace. É chamada para toda matriz de dimensão maior
    ou igual a 3. Como a linha escolhida é sempre a primeira, esta nunca entra
    na nova matriz, bem como a coluna do elemento atual.'''

    nova_matriz = []
    for j in range(1, len(matriz)):
        nova_linha = []
        for k in range(len(matriz[j])):
            if k != coluna:
                nova_linha.append(matriz[j][k])
            else:
                pass
        nova_matriz.append(nova_linha)
    return nova_matriz


def mensagem_final(qtd, n_dim, det):
    '''Imprime a mensagem final, que contém a quantidade de matrizes usadas
    na operação, a dimensão do objeto e o fator multiplicativo de seu volume
    (isto é, o determinante do produto das matrizes).'''

    print(f'Após as {qtd} transformações, o objeto {n_dim}-dimensional '
          f'teve o volume multiplicado no valor {det}.')


def main():
    '''Código principal.'''
    det_total = 1
    qtd_matrizes = int(input())
    d_matriz = int(input())
    for i in range(qtd_matrizes):
        matriz_atual = []
        for j in range(d_matriz):
            matriz_atual.append(input().split())
        det_atual = determinante_rec(matriz_atual)
        det_total *= det_atual
    mensagem_final(qtd_matrizes, d_matriz, det_total)


if __name__ == '__main__':
    main()
