# lab6 by heusmat
class Mapa:
    '''O mapa recebe o número de salas e o número de itens, para que
    as salas e itens sejam criados em quantidades corretas.'''

    def __init__(self, num_salas, num_itens):
        self.num_salas = num_salas
        self.num_itens = num_itens


class Sala:
    '''Os atributos do objeto da classe Sala (número da sala,
    item que ela contém e a lista das 4 salas adjacentes a ela)
    são atualizados cada vez que o personagem muda de sala
    (veja na função mudar_sala).'''

    def __init__(self, numero, item, salas_adj):
        self.numero = numero
        self.item = item
        self.salas_adj = salas_adj


class Clone:
    '''O objeto da classe Clone, sala_do_clone, possui apenas
    o atributo número, para armazenar em que sala o clone está.'''

    def __init__(self, numero):
        self.numero = numero


class Inventario:
    '''O inventário recebe dois atributos: sua capacidade e
    a lista de itens pegos pelo personagem. Enquanto a capacidade
    for maior que a quantidade de itens pegos, ou seja, tem espaço
    livre, alguma coisa é coletada (ver função pegar_itens_e_opcoes).'''

    def __init__(self, capacidade, itens_pegos):
        self.capacidade = capacidade
        self.itens_pegos = itens_pegos


def criar_salas():
    '''A função cria salas de acordo com a quantidade expressa em
    mapa.num_salas. Cada sala criada é uma lista, que contém seu número,
    as quatro salas adjacentes, e o item que ela possui. Toda sala
    começa com item = 'nenhum', que pode ser alterado na função
    colocar_itens.'''

    global lista_de_salas
    nova_sala = input().split()
    nova_sala.append('nenhum')
    for i in range(len(nova_sala) - 1):  # elementos numéricos str --> int
        nova_sala[i] = int(nova_sala[i])
    lista_de_salas.append(nova_sala)


def colocar_itens():
    '''Essa função cria uma lista com dois elementos, sendo o [0]
    o número da sala em que o item [1] será adicionado (na verdade,
    o atributo [5] da sala, por padrão 'nenhum', é substituído).'''

    global lista_de_salas
    sala_e_item = input().split()
    sala_e_item[0] = int(sala_e_item[0])
    numero_da_sala = sala_e_item[0]
    lista_de_salas[numero_da_sala][5] = sala_e_item[1]


def mudar_sala(numero_da_sala):
    '''Atualiza os atributos do objeto sala_atual (classe Sala),
    de acordo com a sala apontada no parâmetro numero_da_sala.
    Após isso, duas funções são chamadas: checar_sala e
    pegar_itens_e_opcoes.'''

    print(f'Mover para sala {numero_da_sala}')
    global sala_atual
    sala_atual = Sala(numero=numero_da_sala,
                      item=lista_de_salas[numero_da_sala][5],
                      salas_adj=lista_de_salas[numero_da_sala][1:5])
    checar_sala()
    pegar_itens_e_opcoes()


def checar_sala():
    '''Faz a checagem se a sala para qual o personagem se moveu é
    a mesma do clone. Caso negativo, é pulada. Caso positivo, verifica
    se a lista de itens do inventário (inventario.itens_pegos) possui
    a str 'espada', se sim, a mensagem de vitória é impressa e a execução do
    programa é terminada, se não, a mensagem de derrota é impressa e o
    programa é terminado.'''

    if sala_atual.numero == sala_do_clone.numero:
        item = ''
        for i in range(len(inventario.itens_pegos)):
            item = inventario.itens_pegos[i]
            if item == 'espada':
                print('Você derrotou o clone maligno com a espada'
                      ' mágica! Com a Sarah no reino o mundo pode voltar'
                      ' ao equilíbrio.\nPARABÉNS!')
                exit()
        print('Infelizmente você encontrou o clone sem a espada das fadas e '
              'foi derrotado. Tente novamente...')
        exit()


def pegar_itens_e_opcoes():
    '''A função checa, primeiramente, se a sala para qual o personagem
    se moveu tem algum item. Caso não possua, são impressos seu
    número e a lista de salas adjacentes a ela. Caso possua, são
    impressos seu número, o item que ela contém e a lista de salas
    adjacentes.
    Então, é feita uma nova checagem: caso o inventário
    tenha espaços livres, o item da sala é adicionado à lista
    inventario.itens_pegos, caso não tenha, é impresso 'inventário cheio'
    A última checagem verifica se o item pego é a poção letal. Se sim,
    é impressa mensagem de derrota e o programa é encerrado. Se
    não, a execução continua normalmente.'''

    if sala_atual.item != 'nenhum':
        print(f'Você está na sala de número {sala_atual.numero} ela contém um '
              f'baú com {sala_atual.item} e dela você pode ir para as salas '
              f'{sala_atual.salas_adj}')
        print(f'Pegar {sala_atual.item}')
        if inventario.capacidade > len(inventario.itens_pegos):
            inventario.itens_pegos.append(sala_atual.item)
            print(f'{sala_atual.item} adicionado ao inventário')
            lista_de_salas[sala_atual.numero][5] = 'nenhum'
            if sala_atual.item == 'poção':
                print('Você pegou a poção da morte e virou pó instantaneamente.'
                      ' Tente novamente...')
                exit()
        else:
            print('Inventário cheio!')
    else:
        print(f'Você está na sala de número {sala_atual.numero} e dela você '
              f'pode ir para as salas {sala_atual.salas_adj}')


qtd_salas = int(input())
mapa = Mapa(num_salas=qtd_salas, num_itens=None)

lista_de_salas = []
for i in range(mapa.num_salas):
    criar_salas()
qtd_itens = int(input())
mapa = Mapa(num_salas=qtd_salas, num_itens=qtd_itens)
for i in range(mapa.num_itens):
    colocar_itens()

n_sala_do_clone = int(input())
sala_do_clone = Clone(numero=n_sala_do_clone)

sala_inicial = int(input())
sala_atual = Sala(numero=lista_de_salas[sala_inicial][0],
                  item=lista_de_salas[sala_inicial][5],
                  salas_adj=lista_de_salas[sala_inicial][1:5])

inventario = Inventario(capacidade=int(input()), itens_pegos=[])

print('Bem-vindo as Aventuras de Sarah 2.0\n'
      'Sarah acorda no saguão do antigo castelo de sua família,ela tem a '
      'oportunidade única de derrotar o seu clone maligno que se apoderou do '
      'reino.\nPara isso ela deve encontrar o baú da sua família que contém '
      'a espada mágica que apenas a verdadeira herdeira pode utilizar.\n'
      'Na sala onde está Sarah vê várias portas. Qual é a sua próxima ação?')
print(f'DEBUG - O clone está na sala: {sala_do_clone.numero}')
checar_sala()
pegar_itens_e_opcoes()

ordem_de_salas = input().split()
for i in range(len(ordem_de_salas)):  # elementos numéricos str --> int
    ordem_de_salas[i] = int(ordem_de_salas[i])

for i in range(len(ordem_de_salas)):
    mudar_sala(ordem_de_salas[i])
