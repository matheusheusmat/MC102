# lab8 by heusmat
from datetime import timedelta, date


def modificar_estoque():
    '''Função chamada no modo_de_operacao = 1.
    Repete-se quantas vezes estiver descrito em qtd_operacoes.

    Em cada repetição, define-se se há uma adição ao estoque ou uma subtração.
    Caso haja adição e o produto ainda não exista, é adicionado um par chave-
    -valor, com o nome do produto sendo a chave e o valor recebe uma tupla
    formada por quantidade, categoria, preço e data de validade, nessa ordem.
    Se o nome do produto já existe no dicionário, a tupla é sobrescrita.

    Caso haja subtração, terá uma tentativa de subtrair de certa chave uma
    quantidade inserida. Se a tentativa for bem sucedida (a chave existe e
    a quantidade retirada é menor ou igual à em estoque), será impresso
    'SUCCESS' e a quantidade será retirada do estoque. Se uma das
    duas condições anteriores não for cumprida, será impresso 'ERROR'
    e o estoque permanecerá inalterado.'''

    qtd_operacoes = int(input())
    for i in range(qtd_operacoes):
        produto = input().split()
        if produto[0] == '0':  # adiciona ao estoque
            estoque[produto[1]] = int(produto[2]), produto[3], float(produto[4]), produto[5]
        if produto[0] == '1':  # retira do estoque
            try:
                nome_produto = produto[1]
                lista_do_produto = estoque[nome_produto]
                lista_do_produto = list(lista_do_produto)
                qtd_retirada = int(produto[2])
                if qtd_retirada > lista_do_produto[0]:
                    print('ERROR')
                else:
                    lista_do_produto[0] -= qtd_retirada
                    estoque[nome_produto] = tuple(lista_do_produto)
                    print('SUCCESS')
            except(KeyError):
                print('ERROR')


def modo_de_caixa():
    '''Função chamada no modo_de_operacao = 1.
    Repete-se quantas vezes estiver descrito em qtd_operacoes.

    Pede-se uma lista com dois itens: o nome do produto comprado
    e a quantidade comprada. É buscado, então, no dicionário 'estoque'
    a chave correspondente ao nome e, dele, é subtraído a quantidade
    comprada. Também soma-se ao 'saldo' a multiplicação entre a quantidade
    comprada e o preço unitário do produto, isto é, o valor final da
    compra.'''

    global saldo
    qtd_operacoes = int(input())
    for i in range(qtd_operacoes):
        produto_comprado = input().split()
        nome_prod_comprado = produto_comprado[0]
        lista_do_produto = list(estoque[nome_prod_comprado])
        qtd_comprada = int(produto_comprado[1])
        preco_do_produto = lista_do_produto[2]
        saldo += qtd_comprada * preco_do_produto
        lista_do_produto[0] -= qtd_comprada
        estoque[nome_prod_comprado] = tuple(lista_do_produto)


def imprimir_relatorio():
    '''Função chamada no modo_de_operacao = 1.
    Apenas pode ser rodada uma vez, após isso, o programa se encerra.
    No início, é pedida a 'data_atual' da operação.

    A função é dividida em 4 partes, 'ESTOQUE', 'SALDO', 'REPOSICAO' e
    'PROMOCAO'.
    Em todo caso, imprime '* ESTOQUE', que fornece uma lista dos produtos
    em estoque, isto é, cuja quantidade em estoque não seja 0, em ordem
    alfabética de categoria.
    Também sempre imprime '* SALDO', que mostra o valor total arrecadado
    em todas as vendas.
    Caso haja item no dicionário 'estoque' cuja quantidade é igual a
    0, será impresso '* REPOSICAO' e, abaixo, os itens em ordem alfabética.
    Por fim, caso haja algum item cuja data de vencimento esteja a 7 dias
    ou menos da data atual, é impresso '* PROMOCAO' e o(s) item(ns) são
    impressos.'''

    global data_atual
    global categorias
    global contador_itens_verificados
    data_atual = input()
    categorias = []
    data_atual = formatar_datas(data_atual)
    contador_itens_verificados = 0
    lista_de_reposicao = []
    print('* ESTOQUE')
    for chave in sorted(estoque):
        criar_lista_de_categorias(estoque[chave])

    for chave in sorted(estoque):  # item em qtd 0 entra na lista de reposicao
        if estoque[chave][0] == 0:
            lista_de_reposicao.append(chave)

    for categoria in sorted(categorias):
        contador_itens_verificados = 0
        for chave in sorted(estoque):
            if estoque[chave][0] != 0 and estoque[chave][1] == categoria:
                printar_categorias(chave, categoria)

    print('* SALDO {:.2f}'.format(saldo))

    if len(lista_de_reposicao) > 0:
        print('* REPOSICAO')
        for l in range(len(lista_de_reposicao)):
            print(lista_de_reposicao[l])

    contador_itens_verificados = 0
    for chave in sorted(estoque):
        if estoque[chave][0] != 0:
            definir_promocao(chave)


def formatar_datas(data):
    '''Transforma as strings de datas de cada produto e a data_atual em
    formato legível pela biblioteca datetime.'''

    ano = int(data[4:])
    mes = int(data[2:4])
    dia = int(data[:2])
    return date(ano, mes, dia)


def criar_lista_de_categorias(produto):
    '''Cria uma lista com todas as categorias de produtos, sem repetição.'''

    global contador_itens_verificados
    if contador_itens_verificados == 0:
        categorias.append(produto[1])
    categoria_atual = produto[1]
    for j in range(len(categorias)):
        if categoria_atual == categorias[j]:
            adiciona = False
            break
        else:
            adiciona = True
    if adiciona:
        categorias.append(categoria_atual)
    contador_itens_verificados += 1


def printar_categorias(chave, categoria):
    '''Todos os produtos em estoque serão verificados por essa função.
    Se ele for o primeiro de sua categoria ao entrar, serão impressos sua
    categoria e, abaixo, o nome do item e quantidade.
    Para os demais da categoria, serão impressos apenas o nome do
    item e quantidade.'''

    global contador_itens_verificados
    if contador_itens_verificados == 0:
        print('-', categoria)
    print(chave, estoque[chave][0])
    contador_itens_verificados += 1


def definir_promocao(chave):
    '''Todos os produtos em estoque serão verificados por essa função.
    A função verifica se a diferença entre a data_atual e a data de
    vencimento do produto é menor ou igual a 7 dias. Caso não, nada é
    feito. Caso sim, e ele for o primeiro, é impresso '* PROMOCAO' e
    seu nome é impresso, e caso não for o primeiro, apenas seu nome é
    impresso.'''

    global contador_itens_verificados
    data_de_vencimento = formatar_datas(estoque[chave][3])
    if (data_de_vencimento - data_atual) <= timedelta(days=7):
        if contador_itens_verificados == 0:
            print('* PROMOCAO')
        print(chave)
        contador_itens_verificados += 1


def main():
    '''Código principal.'''

    global saldo
    global estoque
    saldo = 0.00
    estoque = {}
    modo_de_operacao = int(input())
    while modo_de_operacao != 0:
        if modo_de_operacao == 1:
            modificar_estoque()
            modo_de_operacao = int(input())
        else:
            modo_de_caixa()
            modo_de_operacao = int(input())
    imprimir_relatorio()


if __name__ == '__main__':
    main()
