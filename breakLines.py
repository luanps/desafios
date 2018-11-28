import argparse

'''funcao quebra de linhas: 
    trata sequencialmente substrings de tamanho maximo 'maxChar'. 
    Caso ultimo caractere da substring seja espaco, salva substring
    no vetor 'result'. Caso contrario, verifica caractere anterior
    (endLine -= 1) ate satisfazer a condicao. A execucao encerra quando
    substring for menor que 'maxChar'.
'''
def breakLine(lines,maxChar):
    result = []
    line = [x.strip('\r\n') for x in lines]
    line = ' '.join(str(x) for x in line)
    startLine = 0
    endLine = maxChar
    while len(line) > 0:
        #se ultima substring, armazena-a e encerra funcao
        if len(line) < endLine:
            result.append(line)
            return result
        else:
            #se ultimo char da substring nao for espaco, compara o
            # char anterior para quebra de linha
            while ' ' != line[endLine]:
                endLine-=1
            #ultimo char da substring eh espaco, armazene-a
            result.append(line[startLine:endLine])
            line = line[endLine:]

            #se a substring comecar com espaco, elimine-o:
            if line[0] == ' ':
                line = line[1:]
                endLine+=1
            endLine = maxChar


'''funcao indentacao de texto:
    insere espacos sequencialmente ' ' apos cada palavra de
    dada substring ate que 
    satisfaca a condicao: tamanho substring == maxChar
'''
def indentation(lines,maxChar):
    result = []

    for line in lines:
        #se substring encerrar em ' ', ignore-o
        if line[-1] == ' ':
            line = line[:-1]

        #qtde de espacos para preencher substring
        diff = maxChar - len(line) 

        i = 0
        words = line.split()
        while diff:
            #nao insere espaco apos ultima palavra
            if i >= len(words)-1:
                i=0
            words[i] = words[i]+' '
            i+=1
            diff-=1
        #insere espacos apos palavra i
        result.append(' '.join(words))
    return result

#recebe parametros de entrada
parser = argparse.ArgumentParser()
parser.add_argument("f",help="Texto a ser formatado")
parser.add_argument("maxChar",type=int,
        help="Numero maximo de caracteres por linha")
parser.add_argument("-i",help="-i 1 para indentacao de texto")
args = parser.parse_args()

#leitura do arquivo de texto
try:
    with open(args.f,'r') as f:
        lines = f.readlines()
except Exception as e:
    print(getattr(e,'message',repr(e)))

#funcao quebra de linhas 
result = breakLine(lines,int(args.maxChar))

#funcao de indentacao
if args.i:
    result = indentation(result,args.maxChar)

#saida padrao
print('\n'.join(result))
