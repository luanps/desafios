import argparse

def breakLine(lines,maxChar):
    result = []
    line = [x.strip('\r\n') for x in lines]
    line = ' '.join(str(x) for x in line)
    startLine = 0
    endLine = maxChar
    while len(line) > 0:
        if len(line) < endLine:
            result.append(line)
            return result
        else:
            while ' ' != line[endLine]:
                endLine-=1
            result.append(line[startLine:endLine])
            line = line[endLine:]
            if line[0] == ' ':
                line = line[1:]
                endLine+=1
            endLine = maxChar

def indentation(lines,maxChar):
    result = []
    for line in lines:
        if line[-1] == ' ':
            line = line[:-1]
        diff = maxChar - len(line) 
        i = 0
        words = line.split()
        while diff:
            if i >= len(words)-1:
                i=0
            words[i] = words[i]+' '
            i+=1
            diff-=1
        result.append(' '.join(words))
    return result

parser = argparse.ArgumentParser()
parser.add_argument("f",help="Parse text to be formatted")
parser.add_argument("maxChar",type=int,help="Parse max number of characters per line")
parser.add_argument("-i",help="-i for text identation")
args = parser.parse_args()

try:
    with open(args.f,'r') as f:
        lines = f.readlines()
except Exception as e:
    print(getattr(e,'message',repr(e)))

result = breakLine(lines,int(args.maxChar))

if args.i:
    result = indentation(result,args.maxChar)

print('\n'.join(result))
