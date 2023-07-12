#lab3 by heusmat
q_frascos = int(input())
tx_vib = float(input())
c_solv = int(input())
c_prog = int(input())
cont_1 = 1
indice_i = 1
q_vib = tx_vib * indice_i + tx_vib * c_solv
s_parcial = q_vib

while cont_1 <= q_frascos:
    print('{:.0f} {:.2f} {:.2f}'.format(cont_1, q_vib, s_parcial))
    cont_1 += 1
    indice_i += 1
    q_vib = tx_vib * indice_i + tx_vib * c_solv
    s_parcial += q_vib
s_final = s_parcial - q_vib
print('{:.2f}'.format(s_final))

v_prog = 0
cont_2 = 0
while v_prog + c_prog <= s_final:
    cont_2 += 1
    v_prog = c_prog * cont_2
    if v_prog <= s_final:
        print(v_prog)
        
print(cont_2)
print('BATERIA DE TESTES TERMINADA')






