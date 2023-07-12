# lab11 by heusmat

def ler_arquivos():
    '''Abre os arquivos .txt conforme dado na entrada e extrai as informações:
    número de identificação, título, quantidade de leitores totais, quantidade
    de leitores que foram até o final da notícia, quantidade de cliques em
    anúncios, tempo médio de leitura e quantidade de parágrafos.
    Também cria um dicionário com esses valores, para facilitar a criação
    do relatório final (cálculo das médias e dos maiores valores).
    Ao final, acessa a função gerar_relatorio_de arquivo.'''

    nome_arquivo = input()
    arquivo = open(nome_arquivo, 'r', encoding='utf-8')
    nId = int(arquivo.readline().strip(': nId\n'))
    titulo = arquivo.readline().strip(': titulo\n')
    qtdLeitores = int(arquivo.readline().strip(': qtdLeitores\n'))
    qtdLeitoresFinal = int(arquivo.readline().strip(': qtdLeitoresFinal\n'))
    qtdCliques = int(arquivo.readline().strip(': qtdCliques\n'))
    tempo = int(arquivo.readline().strip(': tempo\n'))
    qtdParagrafos = 0
    for linha in arquivo:
        if '\n' in linha:
            qtdParagrafos += 1
    arquivo.close()
    dicionario_arquivos[nId] = [titulo, qtdLeitores, qtdLeitoresFinal,
                                qtdCliques, tempo, qtdParagrafos]
    gerar_relatorio_de_arquivo(nId, qtdLeitores, qtdLeitoresFinal,
                               qtdCliques, tempo)


def gerar_relatorio_de_arquivo(nId, qtdLeitores, qtdLeitoresFinal,
                               qtdCliques, tempo):

    '''Gera o relatório individual para o arquivo aberto, de nome
    'relatorio_nId.txt', onde nId é o número de identificação da notícia,
    no mesmo diretório'''

    rel_arquivo = open(f'relatorio_{nId}.txt', 'x')
    rel_arquivo.write(f'nId: {nId}\n')
    rel_arquivo.write(f'qtdLeitores: {qtdLeitores}\n')
    rel_arquivo.write(f'qtdLeitoresFinal: {qtdLeitoresFinal}\n')
    rel_arquivo.write(f'qtdCliques: {qtdCliques}\n')
    rel_arquivo.write(f'tempo: {tempo}')
    rel_arquivo.close()


def gerar_medias():
    '''Usa os dados contidos no dicionario_arquivos para calcular as médias
    de qtdLeitores, qtdCliques e qtdParagrafos, médias essas que serão
    usadas na criação do relatório final.'''

    global media_qtdLeitores
    global media_qtdCliques
    global media_qtdParagrafos

    qtd_noticias = len(dicionario_arquivos)
    soma_qtdLeitores = 0
    soma_qtdCliques = 0
    soma_qtdParagrafos = 0
    for i in dicionario_arquivos:
        soma_qtdLeitores += dicionario_arquivos[i][1]
        soma_qtdCliques += dicionario_arquivos[i][3]
        soma_qtdParagrafos += dicionario_arquivos[i][5]
    media_qtdLeitores = soma_qtdLeitores // qtd_noticias
    media_qtdCliques = soma_qtdCliques // qtd_noticias
    media_qtdParagrafos = soma_qtdParagrafos // qtd_noticias


def gerar_maiores_qtds():
    '''Usa os dados contidos no dicionario_arquivos para determinar qual
    das notícias possui maior qtdLeitores, qtdLeitoresFinal e o maior tempo
    médio de leitura.'''

    global titulo_maior_qtdLeitores
    global maior_qtdLeitores
    global titulo_maior_qtdLeitoresFinal
    global maior_qtdLeitoresFinal
    global maior_tempo

    titulo_maior_qtdLeitores = None
    maior_qtdLeitores = 0
    for i in dicionario_arquivos:  # Maior qtdLeitores
        if dicionario_arquivos[i][1] > maior_qtdLeitores:
            titulo_maior_qtdLeitores = dicionario_arquivos[i][0]
            maior_qtdLeitores = dicionario_arquivos[i][1]

    titulo_maior_qtdLeitoresFinal = None
    maior_qtdLeitoresFinal = 0
    for j in dicionario_arquivos:  # Maior qtdLeitoresFinal
        if dicionario_arquivos[j][2] > maior_qtdLeitoresFinal:
            titulo_maior_qtdLeitoresFinal = dicionario_arquivos[j][0]
            maior_qtdLeitoresFinal = dicionario_arquivos[j][2]

    maior_tempo = 0
    for k in dicionario_arquivos:  # Maior tempo médio
        if dicionario_arquivos[k][4] > maior_tempo:
            maior_tempo = dicionario_arquivos[k][4]


def gerar_relatorio_final():
    '''Gera o arquivo relatorio_final.txt, que contém, respectivamente,
    a média de todos os qtdLeitores das notícias, o título da notícia
    de maior qtdLeitores e sua quantidade, o título da notícia de maior
    qtdLeitoresFinal e sua quantidade, a média de qtdCliques, o maior
    tempo médio de leitura dentre todas as notícias e a média de parágrafos
    das notícias.'''

    rel_final = open('relatorio_final.txt', 'w')
    rel_final.write(f'{media_qtdLeitores}\n')
    rel_final.write(f'"{titulo_maior_qtdLeitores}" {maior_qtdLeitores}\n')
    rel_final.write(f'"{titulo_maior_qtdLeitoresFinal}" {maior_qtdLeitoresFinal}\n')
    rel_final.write(f'{media_qtdCliques}\n')
    rel_final.write(f'{maior_tempo}\n')
    rel_final.write(f'{media_qtdParagrafos}')
    rel_final.close()


def main():
    '''Código principal.'''

    global dicionario_arquivos
    dicionario_arquivos = {}
    qtd_arquivos = int(input())
    for i in range(qtd_arquivos):
        ler_arquivos()
    gerar_medias()
    gerar_maiores_qtds()
    gerar_relatorio_final()


if __name__ == '__main__':
    main()
