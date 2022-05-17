import random
def carta() :
    k = True
    c = 0
    while( k == True) :
        x = random.randint(0,3)
        y = random.randint(0,12)
        if(baralho[x][y] == ' ') :
            continue
        else :
            c = baralho[x][y]
            baralho[x][y] = ' '
            k = False
    return c
class Mao(object) :
    def __init__(self,cartas) :
        self.cartas = cartas
    def soma(self) :
        c1,c2 = self.cartas
        if(c1 == 'A') :
            return c2 + 11
        elif(c2 == 'A') :
            return c1 + 11
        else :
            return c1 + c2
print("AVISO:")
print("Sempre responda com um núnmero inteiro ou com sim ou não")
print("------------------------------------------------------------------")
print("Bem vindo ao cassinITA!")
print("Vamos jogar Blackjack.")
print("Boa sorte !!")
print("------------------------------------------------------------------")
baralho = [ ['A' , 2 , 3 , 4 , 5 , 6 , 7 , 8 , 9 , 10 , 10 , 10, 10],
            ['A' , 2 , 3 , 4 , 5 , 6 , 7 , 8 , 9 , 10 , 10 , 10, 10],
            ['A' , 2 , 3 , 4 , 5 , 6 , 7 , 8 , 9 , 10 , 10 , 10, 10],
            ['A' , 2 , 3 , 4 , 5 , 6 , 7 , 8 , 9 , 10 , 10 , 10, 10] ]
carteira = int(input("Quantas fichas vai querer? "))
continuar = "sim"
while(continuar == "sim") :
    aposta = int(input("Qual a sua aposta? "))
    if(aposta > carteira) :
        print("Você não tem fichas o suficientes, logo, apostará todas as fichas.")
        aposta = carteira
    jogador = Mao(cartas = [carta() , carta()])
    dealer = Mao(cartas = [carta() , carta()])
    print("Suas cartas:" , jogador.cartas)
    print("Na mão:" , jogador.soma())
    print("Cartas da mesa:", dealer.cartas[0])
    if(jogador.soma() == 21) :
        carteira += aposta
        print("Você ganhou!!")
        print("Agora você está com" , carteira , "fichas")
        resposta = input("Quer jogar novamente? ")
        if(resposta == "sim") :
            continue
        if(resposta == "nao") :
            break
    resposta = input("Mais cartas? ")
    soma = jogador.soma()
    while(resposta == "sim") :
        nova_carta = carta()
        jogador.cartas.append(nova_carta)
        print("Suas cartas :" , jogador.cartas)
        if(jogador.cartas.count(10) == 0 and nova_carta == 'A') :
            soma += 11
        elif(jogador.cartas.count(10) != 0 and nova_carta == 'A') :
            soma += 1
        else :
            soma += nova_carta
        print("Na mão :", soma)
        if(soma > 21) :
            break
        elif(soma == 21) :
            break
        else :
            resposta = input("Quer mais cartas? ")
    soma2 = dealer.soma()
    print("Cartas da banca:" , dealer.cartas)
    if(soma > 21 ) :
        print("A banca ganhou!!")
        carteira -= aposta
        print("Agora você está com" , carteira , "fichas")
    elif(dealer.soma() == 21 or dealer.soma() > soma) :
        print("A banca ganhou")
        carteira -= aposta
        print("Agora você está com" , carteira , "fichas")
    elif(soma == 21) :
        print("Você ganhou!!")
        carteira += aposta
        print("Agora você está com" , carteira , "fichas")
    else :
        while(soma2 < soma) :
            nova_carta = carta()
            dealer.cartas.append(nova_carta)
            print("Cartas da banca" , dealer.cartas)
            if(dealer.cartas.count(10) == 0 and nova_carta == 'A') :
                soma2 += 11
            elif(dealer.cartas.count(10) != 0 and nova_carta == 'A') :
                soma2 += 1
            else :
                soma2 += nova_carta
            print("Na banca :", soma)
        if(soma2 <= 21 and soma2 != soma) :
            print("A banca ganhou!!")
            carteira -= aposta
            print("Agora você está com" , carteira , "fichas")
        else :
            print("Você ganhou!!")
            carteira += aposta
            print("Agora você está com" , carteira , "fichas")
    if(carteira == 0) :
        print("Mais sorte da próxima vez.")
        break
    continuar = input("Mais uma rodada? ")
print("Obrigado por jogar!")