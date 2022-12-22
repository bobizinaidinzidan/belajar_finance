import requests

#x = requests.get('https://ojk-invest-api.vercel.app/api/products')
#data = x.json()    #print the response text (the content of the requested file):
#loop = data['data']         
#for i in loop["products"]:
    #print(i)

#key = '92ea9528dfdf49d7a9e9acc99b9c3cb0'
#api = requests.get(f'https://newsapi.org/v2/top-headlines?category=business&country=id&apiKey={key}')
#dataapi = api.json()
#for i in dataapi['articles']:
#    print(i['content'])

r = requests.get("https://the-lazy-media-api.vercel.app/api/games/review")        
data1 = r.json()        
    
for d in data1:    
    #print(d['title'])
    #print(d['author'])
    #print(d['time'])
    #print(d['desc'])
    key =d['key']  

    r2 = requests.get(f"https://the-lazy-media-api.vercel.app/api/detail/{key}")
    data2 = r2.json()['results']
    data2['content']
        