import urllib.request, json
import argparse
import telepot
import pdb

#quantidade minima de upvotes a ser considerada
threshold = 5000

#config bot Telegram
bot = telepot.Bot('792123714:AAFuyWepk0DZqCE4H1HuNpf1R5GTFth5Qms')

#recebe subreddit e extrai informacoes do JSON reddit
def topThreads(subreddit):

    try:
        #url JSON do subreddit com threads mais votadas as ultimas 24hs
        url = 'https://www.reddit.com/r/%s/top.json?sort=top'%subreddit
        response = urllib.request.urlopen(url)
    except Exception as e:
        print(getattr(e,'message',repr(e)))
        return
    
    data = json.loads(response.read())

    result = []
    linkPrefix = 'https://www.reddit.com'

    #percorre 25 threads mais recentes
    for item in data['data']['children']:
        upvote = item['data']['score']
        #ignora threads com upvotes < limiar(5000)
        if int(upvote) > threshold:
            result.append({
                'upvote' : upvote,
                'title' : item['data']['title'],
                'link' : linkPrefix + item['data']['permalink']
            })
    return result

parser = argparse.ArgumentParser()
parser.add_argument("sub",help='Subreddits separados por ;')
parser.add_argument("-id",help='Chat_id Telegram: Ex: -id 123')
args = parser.parse_args()

subreddits = args.sub.split(';')
if args.id:
    pdb.set_trace()

for sub in subreddits:
    print(sub)
    '''if args.s:
        res = runScrapy(sub)
        pdb.set_trace()
    else:'''
    print(topThreads(sub))
