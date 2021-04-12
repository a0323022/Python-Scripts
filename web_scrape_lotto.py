import requests
res = requests.get('https://www.lotterycorner.com/il/lotto/2021')


print(type(res))

#len(res.text)

#print(res.text)

#figure out how URL progresses on each "next"
#read the pages in a while? loop
#if response is a 'fail', exit loop, otherwise do stuff

#page is loaded in a text.  Need to figure out how to identify numbers"
#

