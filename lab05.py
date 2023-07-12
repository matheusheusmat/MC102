# lab5 by heusmat
def gerador_num_aleat(x, intervalo_k):
    global num_aleat

    y = (7 * x + 111) % 1024
    print(f"MENSAGEM DEBUG - número gerado: {y}")
    num_aleat = y
    return y % intervalo_k


def checador_de_vida():
    global atributos_sarah
    global atributos_clone

    if atributos_sarah[0] <= 0:
        print("Sarah foi derrotada...")
    elif atributos_clone[0] <= 0:
        print("O clone foi derrotado! Sarah venceu!\nFIM - PARABENS")


def soco():
    global num_aleat
    global contador_turno
    global atributos_clone
    global atributos_sarah

    if contador_turno % 2 != 0:  # ataque de Sarah
        dano_base = atributos_sarah[1] - atributos_clone[2]
        multiplicador_soco = gerador_num_aleat(num_aleat, 3)
        dano_total = dano_base * multiplicador_soco
        if dano_total <= 0:
            dano_total = 0
        atributos_clone[0] -= dano_total
        print(f"O clone sofreu {dano_total} pontos de dano!")
        checador_de_vida()

    else:  # ataque do Clone
        dano_base = atributos_clone[1] - atributos_sarah[2]
        multiplicador_soco = gerador_num_aleat(num_aleat, 3)
        dano_total = dano_base * multiplicador_soco
        if dano_total <= 0:
            dano_total = 0
        atributos_sarah[0] -= dano_total
        print(f"Sarah sofreu {dano_total} pontos de dano!")
        checador_de_vida()


def arremesso_de_facas():
    global contador_turno
    global num_aleat
    global atributos_clone
    global atributos_sarah

    if contador_turno % 2 != 0:  # ataque de Sarah
        quantidade_facas = gerador_num_aleat(num_aleat, 6)
        dano_total = 0
        for golpe_i in range(1, quantidade_facas + 1):
            dano_parcial = atributos_sarah[1] // 3 ** golpe_i
            atributos_clone[0] -= dano_parcial
            dano_total += dano_parcial
        print(f"O clone sofreu {dano_total} pontos de dano!")
        checador_de_vida()

    else:  # ataque do clone
        quantidade_facas = gerador_num_aleat(num_aleat, 6)
        dano_total = 0
        for golpe_i in range(1, quantidade_facas + 1):
            dano_parcial = atributos_clone[1] // 3 ** golpe_i
            atributos_sarah[0] -= dano_parcial
            dano_total += dano_parcial
        print(f"Sarah sofreu {dano_total} pontos de dano!")
        checador_de_vida()


def invocacao_de_fada():
    global contador_turno
    global num_aleat
    global atributos_clone
    global atributos_sarah

    if contador_turno % 2 != 0:  # turno de Sarah
        p_vida_ganhos = gerador_num_aleat(num_aleat, 100)
        atributos_sarah[0] += p_vida_ganhos
        efeito_sec = gerador_num_aleat(num_aleat, 1024)
        print(f"Sarah ganhou {p_vida_ganhos} pontos de vida!")
        if efeito_sec < 100:
            if efeito_sec % 2 != 0:
                atributos_sarah[1] += efeito_sec
                print(f"Sarah ganhou {efeito_sec} pontos de ataque!")
            elif efeito_sec % 2 == 0 and efeito_sec != 0:
                atributos_sarah[2] += efeito_sec
                print(f"Sarah ganhou {efeito_sec} pontos de defesa!")
        elif efeito_sec >= 1019:
            print('''O quê? A fada trouxe um monstro gigante com ela!
O Clone e o castelo foram destruídos,
e Sarah agora tem um novo pet.
FINAL SECRETO - PARABENS???''')
            atributos_clone[0] = 0

    else:  # turno do clone
        p_vida_ganhos = gerador_num_aleat(num_aleat, 100)
        atributos_clone[0] += p_vida_ganhos
        efeito_sec = gerador_num_aleat(num_aleat, 1024)
        print(f"O clone ganhou {p_vida_ganhos} pontos de vida!")
        if efeito_sec < 100:
            if efeito_sec % 2 != 0:
                atributos_clone[1] += efeito_sec
                print(f"O clone ganhou {efeito_sec} pontos de ataque!")
            elif efeito_sec % 2 == 0 and efeito_sec != 0:
                atributos_clone[2] += efeito_sec
                print(f"O clone ganhou {efeito_sec} pontos de defesa!")
        elif efeito_sec >= 1019:
            print('''O quê? A fada trouxe um monstro gigante com ela!
Sarah foi derrotada...''')
            atributos_sarah[0] = 0


contador_turno = 1
atributos_sarah = input().split(' ')
atributos_clone = input().split(' ')

for i in range(len(atributos_clone)):  # converte str em int
    atributos_sarah[i] = int(atributos_sarah[i])
    atributos_clone[i] = int(atributos_clone[i])

num_aleat = int(input())

while atributos_sarah[0] > 0 and atributos_clone[0] > 0:
    ataque = input()
    if ataque == "soco":
        soco()
    elif ataque == "facas":
        arremesso_de_facas()
    elif ataque == "fada":
        invocacao_de_fada()
    contador_turno += 1
