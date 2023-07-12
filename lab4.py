#lab4 by heusmat
lista_operacao = []
lista_operacao = input().split(' ')
resultados = []
quant_de_resultados = -1

while lista_operacao[0] != '0':

    lista_operacao[1] = int(lista_operacao[1])
    lista_operacao[2] = int(lista_operacao[2])

    if lista_operacao[0] == '+':
        res_soma = lista_operacao[1] + lista_operacao[2]
        resultados.append(res_soma)

    elif lista_operacao[0] == '-':
        res_sub = lista_operacao[1] - lista_operacao[2]
        resultados.append(res_sub)

    elif lista_operacao[0] == '*':
        res_prod = lista_operacao[1] * lista_operacao[2]
        resultados.append(res_prod)

    elif lista_operacao[0] == '/':
        res_div = lista_operacao[1] // lista_operacao[2]
        resto = lista_operacao[1] % lista_operacao[2]
        elemento_div = ('{} {}'.format(res_div, resto))
        resultados.append(elemento_div)

    elif lista_operacao[0] == ';':
        congr = lista_operacao[1] - lista_operacao[2]
        if congr == 0:
            lista_div_congr = 0
        else:
            if congr < 0:
                congr = -1 * congr
            lista_div_congr = 1
            for div_congr in range(2, congr + 1):
                if congr % div_congr == 0:
                    lista_div_congr = ('{} {}'.format(lista_div_congr, div_congr))
        resultados.append(lista_div_congr)

    quant_de_resultados += 1    
    lista_operacao = input().split(' ')

for printar_lista in range(0, quant_de_resultados + 1):
    print(resultados[printar_lista])