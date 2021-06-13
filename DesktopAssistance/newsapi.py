import requests
import json
url = ('http://newsapi.org/v2/top-headlines?'
       'country=us&'
       'apiKey=yourapikey')
response = requests.get(url)
data = response.content
jdata = json.loads(data.decode())
article=jdata["articles"]
result=[]
for item in article:
    title=item["title"]
    result.append(title)

for i in range(len(result)):
    my_json = json.dumps(result[i])
    print(my_json)
