#lab2 by heusmat

print('*Que página de meme do Instagram você é?*')
idade = int(input('Qual a sua idade?\n'))
print(idade)

if idade > 125 or idade < 0:
    print('Erro: entrada inválida')

elif idade < 25:
    seg = int(input('Quantos segundos são necessários para saber se um vídeo é bom?\n'))
    print(seg)
    if seg < 0:
        print('Erro: entrada inválida')
    elif seg <= 5:
        print('RESULTADO\nVocê deveria estar no TikTok')
    elif seg > 5:
        print('RESULTADO\nSua página de memes é: @meltmemes') 

elif 25 <= idade <= 40:
    banda = input('Qual banda você gosta mais?\n')
    if banda != 'A' and banda != 'B' and banda != 'C' and banda != 'D':
        print('Erro: entrada inválida')
    elif banda == 'A':
        print('A) Matanza')
        print('RESULTADO\nSua página de memes é: @badrockistamemes')
    elif banda == 'B':
        print('B) Iron Maiden')
        print('RESULTADO\nSua página de memes é: @badrockistamemes')
    elif banda == 'C':
        print('C) Imagine Dragons')
        cap = input('São as capivaras os melhores animais da Terra?\n')
        print(cap)
        if cap != 'Sim' and cap != 'Não':
            print('Erro: entrada inválida')
        elif cap == 'Sim':
            print('RESULTADO\nSua página de memes é: @genteboamemes')
        elif cap == 'Não':
            print('RESULTADO\nSua página de memes é: @wrongchoicememes')
    elif banda == 'D':
        print('D) BlackPink')
        cap = input('São as capivaras os melhores animais da Terra?\n')
        print(cap)
        if cap != 'Sim' and cap != 'Não':
            print('Erro: entrada inválida')
        elif cap == 'Sim':
            print('RESULTADO\nSua página de memes é: @genteboamemes')
        elif cap == 'Não':
            print('RESULTADO\nSua página de memes é: @wrongchoicememes')    

elif idade > 40:
    img = input('Que imagem de bom dia você manda no grupo da família?\n')
    if img != 'A' and img != 'B' and img != 'C':
        print(img)
        print('Erro: entrada inválida') 
    elif img == 'A':
        print('A) Bebê em roupa de flor')
        print('RESULTADO\nSua página de memes é: @bomdiabebe')
    elif img == 'B':
        print('B) Gato')
        print('RESULTADO\nSua página de memes é: @kittykatmsgs')
    elif img == 'C':
        print('C) Coração e rosas')
        print('RESULTADO\nSua página de memes é: @bomdiaflordodia')