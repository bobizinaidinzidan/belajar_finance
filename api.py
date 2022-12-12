import requests

x = requests.get('https://ojk-invest-api.vercel.app/api/products')
data = x.json()    #print the response text (the content of the requested file):
loop = data['data']         
for i in loop["products"]:
    print(i)