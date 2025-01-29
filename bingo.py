from random import randint

def equilibrar(numero):
    numero=str(numero)
    dic={
        1:f"0{numero}",
        2:numero
    }
    return dic[len(numero)]


def verificar_numeros(numero, numeros_sorteados):
    numero_equilibrado = equilibrar(numero)
    dic = {}
    for numero_sorteado in numeros_sorteados:
        dic[numero_sorteado] = f"({numero_equilibrado})"
    try:
        return dic[numero]
    except:
        return f" {numero_equilibrado} "


def criar_jogadores_cartelas(dificuldade):
    jogadores ={}
    quantidade_jogadores = 2**dificuldade*2
    numeros_cartelas={}

    for i in range(1,1+quantidade_jogadores):
        jogadores[f'Jogador: {i}'] = []
        numeros_cartelas[f'Jogador: {i}'] = []
        for j in range(2**dificuldade+1):
            jogadores[f'Jogador: {i}'].append([])
            for k in range(1,(2**dificuldade+2)*10,10):
                numero_cartela = randint(k, k + 9)
                while numero_cartela in numeros_cartelas[f'Jogador: {i}']:
                    numero_cartela=randint(k,k+9)
                numeros_cartelas[f'Jogador: {i}'].append(numero_cartela)
                jogadores[f'Jogador: {i}'][j].append(numero_cartela)
    return jogadores

def exibir_cartelas(jogadores,numeros_sorteados):
    cartela_formatada=""
    for jogador in jogadores:
        cartela_formatada+=f"\n{jogador}"
        for cartela in jogadores[jogador]:
            cartela_formatada+="\n"
            for numero in cartela:
                cartela_formatada+=verificar_numeros(numero,numeros_sorteados)
    print(cartela_formatada)

def exibir_numeros_sorteados(numeros_sorteados):
    mensagem="Dezenas sorteadas até o momento:"
    numeros_sorteados=sorted(numeros_sorteados)
    for numero in numeros_sorteados:
        mensagem+=f" {equilibrar(numero)}"
    print(mensagem)
def verificar_sorteio(numero,numeros_sorteados):
    dic={
        True:1,
        False:0
    }
    return dic[numero in numeros_sorteados]
def verificar_cartelas(jogadores,jogador,numeros_sorteados,dificuldade):
    numeros_cartela_sorteados=0
    list=[]
    for i in range((2**dificuldade+1)*(2**dificuldade+2)):
        list.append(True)
    list.append(False)
    for cartela in jogadores[jogador]:
        for numero in cartela:
            numeros_cartela_sorteados+=verificar_sorteio(numero,numeros_sorteados)
    return list[numeros_cartela_sorteados]
def verificar_ganhar(condicao,jogadores,jogador,numeros_sorteados,dificuldade):
    dic={
        True:verificar_cartelas(jogadores,jogador,numeros_sorteados,dificuldade),
        False:False
    }
    return dic[condicao]
def verificar_jogador_vencedor(condicao,jogador,jogador_vencedor):
    dic={
        True:jogador,
        False:jogador_vencedor
    }
    return dic[condicao]
def jogar(dificuldade,condicao):
    while dificuldade not in [0,1]:
        dificuldade = int(input("Indique qual o modo de jogo:\n0 - RÁPIDO\n1 - DEMORADO\n"))
    jogadores=criar_jogadores_cartelas(dificuldade)
    numeros_sorteados=[]
    jogador_vencedor=""
    while condicao:
        exibir_cartelas(jogadores,numeros_sorteados)
        input("Digite ENTER para continuar")
        numero_sorteado=randint(1,2**dificuldade+2)
        while numero_sorteado in numeros_sorteados:
            numero_sorteado=randint(1,(2**dificuldade+2)*10)
        numeros_sorteados.append(numero_sorteado)
        print(f"=> Última dezena sorteada: {equilibrar(numero_sorteado,)}")
        exibir_numeros_sorteados(numeros_sorteados)
        for jogador in jogadores:
            jogador_vencedor = verificar_jogador_vencedor(condicao, jogador, jogador_vencedor)
            condicao = verificar_ganhar(condicao, jogadores, jogador, numeros_sorteados, dificuldade)
    exibir_cartelas(jogadores, numeros_sorteados)
    print(f"{jogador_vencedor} é o ganhador!")
jogar_novamente=True
while jogar_novamente:
    condicao = True
    jogar(2, condicao)
    dic={
        0:True,
        1:False
    }
    opcao_jogar_denovo=int(input("Você deseja jogar de novo?\n0-Sim\n1-Não"))
    while opcao_jogar_denovo not in [0,1]:
        opcao_jogar_denovo = int(input("Você deseja jogar de novo?\n0-Sim\n1-Não\n"))
    jogar_novamente=dic[opcao_jogar_denovo]
