import requests
#print(requests.__version__)
r = requests.get('http://www.google.com/')
r = requests.get('https://raw.githubusercontent.com/mattypaez/404Lab1/main/requestScript.py')
print(r.text)