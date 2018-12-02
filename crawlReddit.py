import urllib.request, json
import pdb
import argparse

#quantidade minima de upvotes a ser considerada
threshold = 5000

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
args = parser.parse_args()

subreddits = args.sub.split(';')
res = []
for sub in subreddits:
    print(sub)
    print(topThreads(sub))
