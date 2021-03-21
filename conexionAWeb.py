import urllib.request

f = urllib.request.urlopen('https://www.marca.com')

for line in f:
    print(line.decode().strip())



