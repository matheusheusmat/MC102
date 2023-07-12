# lab10 by heusmat

class especie:
    def __init__(self, id_esp, nome_cientifico, lista_caracs):
        self.id_esp = id_esp
        self.nome_cientifico = nome_cientifico
        self.lista_caracts = lista_caracs


class carac:
    def __init__(self, nome_carac, dnaa_1, dnaa_2, lista_pares_dnaa):
        self.nome_carac = nome_carac
        self.dnaa_1 = dnaa_1
        self.dnaa_2 = dnaa_2
        self.lista_pares_dnaa = lista_pares_dnaa


def criar_dic_esp():
    '''Cria o dicionário que contém as espécies. As chaves são os números
    de identificação da espécie. Os valores são, respectivamente, o nome
    científico da espécie e uma lista que contém suas características.'''

    infos_especie = input().split()
    especie_atual = especie(id_esp=int(infos_especie[0]),
                            nome_cientifico=' '.join(infos_especie[1:3]),
                            lista_caracs=infos_especie[4:])
    dic_esp[especie_atual.id_esp] = especie_atual.nome_cientifico, especie_atual.lista_caracts


def criar_dic_carac(j):
    '''Cria o dicionário que contém as características. As chaves são o grau
    de ancestralidade daquela característica (excluindo-se a primeira, que
    é a ancestral), definido pela função numero_de_mutacoes. O valor é o
    nome da característica.'''

    global carac_atual
    carac_atual = carac(nome_carac=input(), dnaa_1=input(),
                        dnaa_2=input(), lista_pares_dnaa=None)
    carac_atual.lista_pares_dnaa = [carac_atual.dnaa_1[x] + carac_atual.dnaa_2[x]
                                    for x in range(len(carac_atual.dnaa_1))]
    if j == 0:
        dic_carac[0] = carac_atual.nome_carac, carac_atual.lista_pares_dnaa
    else:
        dic_carac[numero_de_mutacoes()] = carac_atual.nome_carac, carac_atual.lista_pares_dnaa


def numero_de_mutacoes():
    '''Cria as chaves do dicionário 'dic_carac', de acordo com a quantidade
    de mutações presentes no DNAA da característica. Útil para organizá-las
    em ordem crescente de ancestralidade'''

    num_mutacoes = 0
    for x in range(len(carac_atual.lista_pares_dnaa)):
        if carac_atual.lista_pares_dnaa[x] > dic_carac[0][1][x]:
            num_mutacoes += 1
    return num_mutacoes


def organizar_especies():
    '''Classifica as espécies de acordo com sua característica menos
    ancestral, guardando as informações no dicionário dic_ordenado,
    cujas chaves são as características, em ordem crescente de ancestralidade,
    e o valor é uma lista que, caso a espécie possua esta característica
    como a menos ancestral, é adicionada à ela.'''

    global dic_ordenado
    dic_ordenado = {}
    for x in sorted(dic_carac, reverse=True):
        nova_chave = dic_carac[x][0]
        dic_ordenado[nova_chave] = []
    for w in dic_ordenado:
        for y in sorted(dic_esp):
            for z in dic_esp[y][1]:
                if z == w:
                    dic_ordenado[w].append(str(y) + ' ' + dic_esp[y][0])
                    del dic_esp[y]


def imprimir_final():
    '''Cria uma lista chamada 'lista_de_impressao', que contém
    as informações do dicionário dic_ordenado, porém de trás para frente, pois
    deve-se imprimir em ordem decrescente de ancestralidade.'''

    lista_de_impressao = []
    for x in dic_ordenado.keys():
        for y in range(len(dic_ordenado[x])-1, -1, -1):
            lista_de_impressao.append(dic_ordenado[x][y])
        lista_de_impressao.append('CARACTERÍSTICA: ' + x)
    for z in range(len(lista_de_impressao)-1, -1, -1):
        print(lista_de_impressao[z])


def main():
    '''Código principal.'''
    global dic_esp
    global dic_carac
    dic_esp = {}
    dic_carac = {}
    qtd_especies = int(input())
    for i in range(qtd_especies):
        criar_dic_esp()
    qtd_carac = int(input())
    for j in range(qtd_carac):
        criar_dic_carac(j)
    organizar_especies()
    imprimir_final()


if __name__ == '__main__':
    main()
