# lab13 by heusmat
def organizador_rec(nome_arq_ou_sub, subpasta):
    '''Organiza recursivamente os arquivos e subpastas dados na entrada.
    A cada novo parâmetro dado, a lista de subpastas e arquivos é atualizada e,
    caso alguma das subpastas anteriores estejam na lista, um novo "caminho"
    a partir do anterior é criado. O caso-base para retornar é a presença da
    pasta-raiz no nome da subpasta.'''

    if pasta_raiz in subpasta:
        lista_subs_e_arqs.append(f'{subpasta}_{nome_arq_ou_sub}')
        return f'{subpasta}_{nome_arq_ou_sub}'
    else:
        for item in lista_subs_e_arqs:
            if subpasta in item:
                return organizador_rec(nome_arq_ou_sub, item)


def main():
    '''Código principal, que recebe a pasta-raiz, a quantidade de arquivos
    ou pastas a serem processados e cada arquivo/pasta e a subpasta em que
    se localiza.'''

    global pasta_raiz
    global lista_subs_e_arqs
    lista_subs_e_arqs = []
    raiz_e_n_nomes = input().split()
    pasta_raiz = raiz_e_n_nomes[0]
    qtd_nomes = int(raiz_e_n_nomes[1])
    for i in range(qtd_nomes):
        nome_e_subpasta = input().split()
        nome_arq_ou_sub = nome_e_subpasta[0]
        subpasta = nome_e_subpasta[1]
        print(organizador_rec(nome_arq_ou_sub, subpasta))


if __name__ == '__main__':
    main()
