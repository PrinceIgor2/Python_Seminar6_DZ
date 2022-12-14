# 4 - Дан список URL различных сайтов. Нужно составить список доменных имен сайтов.


domain_list = ['https://dzen.ru/a/Y5cRv6EdHgt6ZBaq/', 
'https://ladoshki.uecard.ru/schoolAdm/preOrderList/',              
'https://schools.school.mosreg.ru/reports/default.aspx?school=22853&year=2022&report=statJournal-school&datefrom=14.12.2022&dateto=14.12.2022',
'https://cont.ws/@Fritzmorgen/2441157',
'https://ozr-shkkurg.edumsko.ru/activity/innovate'           
'https://smotrim.ru/pick/serials?utm_source=internal&utm_medium=tabbar-menu&utm_campaign=tabbar-menu',
'https://e.mail.ru/inbox/?authid=l6zg0f83.8no&back=1%2C1&dwhsplit=s10273.b1ss12743s&from=login&x-login-auth=1&ysclid=l6zg0ejz5e180165402&afterReload=1']


domain_names = list(map(lambda i: i[ : i.find('/')], [i for i in map(lambda i: i.replace('https://', ''), domain_list)] ))
print(f' Список доменных имен: {domain_names}')
