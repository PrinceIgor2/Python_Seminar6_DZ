# 4 - Дан список URL различных сайтов. Нужно составить список доменных имен сайтов.

import urllib.parse

url = "http://python.org"
domain = urllib.parse.urlsplit(url)[1]
print ("The domain name of the url is: ", domain)


