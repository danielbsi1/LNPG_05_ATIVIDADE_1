# Um programa que receba um arquivo como parametro, ver quantas palavras tem, a maior palavra, a vogal mais usada #
# a primeira palavra com "ção", e informar a linha" #


def pedir_arquivo():
    global arquivo_nome
    arquivo_nome = input(str("Ola, digite o caminho do arquivo que você quer que seja analizado: "))


def cont_palavras(arquivo):
    """
    Essa função vai ler o arquivo, "limpar" tudo que não for uma palavra, contar as palvras, e printar quantas são.
    """
    arq = open(arquivo, 'r', encoding='utf-8')
    ler = arq.read()
    divisor = (ler.replace(',', '').replace(';', '').replace(':', '')
               .replace(';', '').replace('|', ' ').replace('\n', '').split(' '))
    num_palavras = len(divisor)
    print(f"Esse arquivo tem {num_palavras} palavras\n")
    arq.close()


def maior_palavra(arquivo):
    """
    Essa função lê o arquivo, acha a maior palavra, e printa ela.
    """
    arq = open(arquivo, 'r', encoding='utf-8')
    ler = arq.read()
    divisor = (ler.replace(',', '').replace(';', '').replace(':', '')
               .replace(';', '').replace('|', ' ').replace('\n', '').split(' '))
    big_palavra = sorted(divisor, key=len)
    print(f"A maior palavra deste arquivo é {big_palavra[-1]}\n")
    arq.close()


def uso_vogal(arquivo):
    """
    Essa função lê o arquivo, conta cada vogal usada, e diz qual é a vogal mais usada.
    """
    arq = open(arquivo, 'r', encoding='utf-8')
    ler = arq.read()
    count_a = 0
    count_e = 0
    count_i = 0
    count_o = 0
    count_u = 0
    for n in ler:
        count_a += ler.count("a")
        count_e += ler.count("e")
        count_i += ler.count("i")
        count_o += ler.count("o")
        count_u += ler.count("u")
    if count_a > count_e and count_i and count_o and count_u:
        return print("A vogal mais usada neste arquivo é A\n")
    elif count_e > count_a and count_i and count_o and count_u:
        return print("A vogal mais usada neste arquivo é E\n")
    elif count_i > count_a and count_e and count_o and count_u:
        return print("A vogal mais usada neste arquivo é I\n")
    elif count_o > count_a and count_i and count_e and count_u:
        return print("A vogal mais usada neste arquivo é O\n")
    elif count_u > count_a and count_i and count_e and count_o:
        return print("A vogal mais usada neste arquivo é u\n")


def achar_cao(arquivo):
    arq = open(arquivo, 'r', encoding='utf-8')
    ler = arq.read()
    divisor = (ler.replace(',', '').replace(';', '').replace(':', '')
               .replace(';', '').replace('|', ' ').replace('\n', '').split(' '))
    for n in divisor:
        if "ção" in n:
            print(f"A primeira aparição de \"ção\" no texto é na palavra {n}")
            break
    arq.close()


def main():
    pedir_arquivo()
    cont_palavras(arquivo=arquivo_nome)
    maior_palavra(arquivo=arquivo_nome)
    uso_vogal(arquivo=arquivo_nome)
    achar_cao(arquivo=arquivo_nome)


main()
