import requests

url = "https://apidojo-yahoo-finance-v1.p.rapidapi.com/auto-complete"

#querystring = {"q":"tesla","region":"US"}
symbols = [ 'ibm']

headers = {
    'x-rapidapi-key': "c0ee649bcfmsh5baf4df487f23a2p1ce3b0jsn505cc6af8573",
    'x-rapidapi-host': "apidojo-yahoo-finance-v1.p.rapidapi.com"
    }

datafile = open('results.txt', 'w')
for symbol in symbols:
    querystring = { "q": symbol }
    print( querystring )
    response = requests.request("GET", url, headers=headers, params=querystring)
    datafile.write(response.text)
    

datafile.close()

print(response.text)