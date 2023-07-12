# lab7 by heusmat
class Foto:
    '''Cria objetos com o atributo prefixo e nome_da_foto, importante
    ao corrigir o nome das fotos sem afetar o prefixo. É atualizada
    nas funções corrige_nome e separar_categorias.'''

    def __init__(self, prefixo, nome_da_foto):
        self.prefixo = prefixo
        self.nome_da_foto = nome_da_foto


def separar_ultimo(lista_fotos):
    '''Quebra a última string da lista em duas: a última foto
    e a foto a ser descartada da lista posteriormente. Esta última é
    armazenada na variável global foto_deletada para ser acessada na
    função descarte_foto.'''

    global foto_deletada
    ultima_foto_e_foto_deletada = lista_fotos[-1].split('/ ')
    ultima_foto = ultima_foto_e_foto_deletada[0]
    foto_deletada = ultima_foto_e_foto_deletada[1]
    del lista_fotos[-1]
    lista_fotos.append(ultima_foto)


def foto_consecutiva(lista_fotos):
    '''Conta qual string aparece mais vezes em sequência.
    Cria duas listas, uma com as strings diferentes e outra com as
    quantidades contadas. Se a string é igual a anterior, soma-se
    1 no respectivo contador. Se a string é diferente, ela é adicionada
    na lista nomes_contados e um novo contador é adicionado à
    lista lista_de_contadores e já soma-se 1.
    Ao final, faz-se a checagem do maior contador na lista.
    É impresso, então, a string cujo índice na lista nomes_contados
    condiz com o índice do maior contador da lista_de_contadores,
    além de seu respectivo contador.'''

    nomes_contados = []
    nome_atual = lista_fotos[0]
    nomes_contados.append(nome_atual)
    nome_anterior = nome_atual
    lista_de_contadores = [0]
    contador = 0
    for i in range(len(lista_fotos)):
        nome_atual = lista_fotos[i]
        if nome_atual == nome_anterior:
            lista_de_contadores[len(nomes_contados) - 1] += 1
            nome_anterior = nome_atual
        else:
            nomes_contados.append(nome_atual)
            contador = 0
            lista_de_contadores.append(contador)
            lista_de_contadores[len(nomes_contados) - 1] += 1
            nome_anterior = nome_atual
    maior_numero = 0
    for i in range(len(lista_de_contadores)):
        if lista_de_contadores[i] > maior_numero:
            maior_numero = lista_de_contadores[i]
            nome_mais_freq = nomes_contados[i]
    print(nome_mais_freq, maior_numero)


def remover_repeticoes(lista_fotos):
    '''Tira as repetições da lista_fotos, dada na entrada.
    Cada vez que uma nova string é testada para ver se já está na
    lista_sem_reps (reps=repetições), se a string já estiver na lista,
    ela não é adicionada e a próxima string já é testada. Caso contrário,
    se todos os itens na lista_sem_reps são diferentes da string
    testada, ela é adicionada.
    Retorna a lista sem repetições, atualizando a lista_fotos.'''

    lista_sem_reps = []
    lista_sem_reps.append(lista_fotos[0])
    for i in range(len(lista_fotos)):
        nome_atual = lista_fotos[i]
        for j in range(len(lista_sem_reps)):
            if nome_atual == lista_sem_reps[j]:
                adiciona = False
                break
            else:
                adiciona = True
        if adiciona:
            lista_sem_reps.append(nome_atual)
    print(len(lista_sem_reps))
    return lista_sem_reps


def corrige_nome(lista_fotos):
    '''Troca letras maiúsculas das strings por minúsculas.
    Também substitui os espaços por traços, para padronização.
    Não altera o prefixo, por ele estar separado em atributo diferente.
    Ao final, retorna lista_corrigida, com as todas as strings
    padronizadas.'''

    lista_corrigida = []
    for i in range(len(lista_fotos)):
        lista_caracteres = []
        foto_atual = Foto(prefixo=lista_fotos[i][:3],
                          nome_da_foto=lista_fotos[i][3:])
        foto_atual.nome_da_foto = foto_atual.nome_da_foto.lower()
        for j in range(len(foto_atual.nome_da_foto)):
            lista_caracteres.append(foto_atual.nome_da_foto[j])
        for k in range(len(lista_caracteres)):
            if lista_caracteres[k] == ' ':
                lista_caracteres[k] = '-'
        prefixo_e_nome = ''.join(lista_caracteres)
        prefixo_e_nome = (foto_atual.prefixo + prefixo_e_nome)
        lista_corrigida.append(prefixo_e_nome)
    return lista_corrigida


def descarte_foto(lista_fotos):
    '''Padroniza a variável foto_deletada seguindo as especificações.
    Cria uma lista auxiliar nova_lista, que não contém a string
    foto_deletada, por comparação com a lista_fotos original. Só são
    adicionadas as strings diferentes de foto_deletada à nova_lista.
    Retorna nova_lista, que atualiza lista_fotos.'''

    nova_lista = []
    global foto_deletada
    lista_caracteres = []
    for i in range(len(foto_deletada)):
        lista_caracteres.append(foto_deletada[i])
    for k in range(3, len(foto_deletada)):
        lista_caracteres[k] = lista_caracteres[k].lower()
    for j in range(len(lista_caracteres)):
        if lista_caracteres[j] == ' ':
            lista_caracteres[j] = '-'
    foto_deletada = ''.join(lista_caracteres)

    for l in range(len(lista_fotos)):
        if lista_fotos[l] != foto_deletada:
            nova_lista.append(lista_fotos[l])
    return nova_lista


def separar_categorias(lista_fotos):
    '''Cria três listas novas, cada uma com uma categoria de fotos, de
    acordo com o prefixo: HA_ CR_ ou CC_. A cada foto testada, o objeto
    foto_atual é atualizado. De acordo com o prefixo, a foto é adicionada
    a uma das três listas. Ao final, imprime as listas criadas.'''

    fotos_aranha = []
    fotos_criminoso = []
    fotos_cena_do_crime = []
    for i in range(len(lista_fotos)):
        foto_atual = Foto(prefixo=lista_fotos[i][:3],
                          nome_da_foto=lista_fotos[i][3:])
        if foto_atual.prefixo == 'HA_':
            fotos_aranha.append(lista_fotos[i])
        elif foto_atual.prefixo == 'CR_':
            fotos_criminoso.append(lista_fotos[i])
        elif foto_atual.prefixo == 'CC_':
            fotos_cena_do_crime.append(lista_fotos[i])
    print(fotos_aranha)
    print(fotos_criminoso)
    print(fotos_cena_do_crime)


def main():
    '''Código principal.'''

    lista_fotos = input().split(', ')
    separar_ultimo(lista_fotos)
    foto_consecutiva(lista_fotos)
    lista_fotos = remover_repeticoes(lista_fotos)
    lista_fotos = corrige_nome(lista_fotos)
    lista_fotos = descarte_foto(lista_fotos)
    separar_categorias(lista_fotos)


if __name__ == "__main__":
    main()
