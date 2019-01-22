import telegram
import requests
from bs4 import BeautifulSoup
import os
import time

my_token = '645804650:AAEFzjMH_sL6fU3oj-k12pCsLexAw8Uyzjs'
bot = telegram.Bot(token=my_token)
updates = bot.getUpdates()
chat_id = "702266940"
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

depart_notice = requests.get('http://computer.cnu.ac.kr/index.php?mid=notice')
depart_notice.encoding = 'utf-8'
depart_html = depart_notice.text
depart_soup = BeautifulSoup(depart_html, 'html.parser')
depart_notice1 = depart_soup.select('td.title > a')
depart_notice2 = depart_soup.select('td.title > a.hx')
menu = depart_soup.select('#gnb > ul > li.active > ul > li:nth-child(1)')
depart_latest1 = depart_notice1[0].text
depart_latest2 = depart_notice2[0].text
with open(os.path.join(BASE_DIR, 'depart_latest1.txt'), 'r+') as f_read:
    before = f_read.read()
    if before != depart_latest1:
        text = menu[0].text + "\n" + depart_latest1 + depart_notice1[0].get('href')
        bot.sendMessage(chat_id=chat_id, text=text)
        with open(os.path.join(BASE_DIR, 'depart_latest1.txt'), 'w+') as f:
            f.write(depart_latest1)
    else:
        pass

with open(os.path.join(BASE_DIR, 'depart_latest2.txt'), 'r+') as f_read:
    before = f_read.read()
    if before != depart_latest2:
        text = menu[0].text + depart_latest2.replace("					", "") + depart_notice2[0].get('href')
        bot.sendMessage(chat_id=chat_id, text=text)
        with open(os.path.join(BASE_DIR, 'depart_latest2.txt'), 'w+') as f:
            f.write(depart_latest2)
    else:
        pass

com_notice = requests.get('http://computer.cnu.ac.kr/index.php?mid=gnotice')
com_notice.encoding = 'utf-8'
com_html = com_notice.text
com_soup = BeautifulSoup(com_html, 'html.parser')
com_notice1 = com_soup.select('td.title > a')
com_notice2 = com_soup.select('td.title > a.hx')
menu = depart_soup.select('#gnb > ul > li.active > ul > li:nth-child(2)')
com_latest1 = com_notice1[0].text
com_latest2 = com_notice2[0].text

with open(os.path.join(BASE_DIR, 'com_latest1.txt'), 'r+') as f_read:
    before = f_read.read()
    if before != com_latest1:
        text = menu[0].text + "\n" + com_latest1 + com_notice1[0].get('href')
        bot.sendMessage(chat_id=chat_id, text=text)
        with open(os.path.join(BASE_DIR, 'com_latest1.txt'), 'w+') as f:
            f.write(com_latest1)
    else:
        pass

with open(os.path.join(BASE_DIR, 'com_latest2.txt'), 'r+') as f_read:
    before = f_read.read()
    if before != com_latest2:
        text = menu[0].text + com_latest2.replace("					", "") + com_notice2[0].get('href')
        bot.sendMessage(chat_id=chat_id, text=text)
        with open(os.path.join(BASE_DIR, 'com_latest2.txt'), 'w+') as f:
            f.write(com_latest2)
    else:
        pass

sa_notice = requests.get('http://computer.cnu.ac.kr/index.php?mid=saccord')
sa_notice.encoding = 'utf-8'
sa_html = sa_notice.text
sa_soup = BeautifulSoup(sa_html, 'html.parser')
sa_notice1 = sa_soup.select('td.title > a')
sa_notice2 = sa_soup.select('td.title > a.hx')
menu = depart_soup.select('#gnb > ul > li.active > ul > li:nth-child(3)')
sa_latest1 = sa_notice1[0].text
sa_latest2 = sa_notice2[0].text

with open(os.path.join(BASE_DIR, 'sa_latest1.txt'), 'r+') as f_read:
    before = f_read.read()
    if before != sa_latest1:
        text = menu[0].text + "\n" + sa_latest1 + sa_notice1[0].get('href')
        bot.sendMessage(chat_id=chat_id, text=text)
        with open(os.path.join(BASE_DIR, 'sa_latest1.txt'), 'w+') as f:
            f.write(sa_latest1)
    else:
        pass

with open(os.path.join(BASE_DIR, 'sa_latest2.txt'), 'r+') as f_read:
    before = f_read.read()
    if before != sa_latest2:
        text = menu[0].text + sa_latest2.replace("					", "") + sa_notice2[0].get('href')
        bot.sendMessage(chat_id=chat_id, text=text)
        with open(os.path.join(BASE_DIR, 'sa_latest2.txt'), 'w+') as f:
            f.write(sa_latest2)
    else:
        pass

job_notice = requests.get('http://computer.cnu.ac.kr/index.php?mid=job')
job_notice.encoding = 'utf-8'
job_html = job_notice.text
job_soup = BeautifulSoup(job_html, 'html.parser')
job_notice1 = job_soup.select('td.title > a')
job_notice2 = job_soup.select('td.title > a.hx')
menu = depart_soup.select('#gnb > ul > li.active > ul > li:nth-child(4)')
job_latest1 = job_notice1[0].text
job_latest2 = job_notice2[0].text

with open(os.path.join(BASE_DIR, 'job_latest1.txt'), 'r+') as f_read:
    before = f_read.read()
    if before != job_latest1:
        text = menu[0].text + "\n" + job_latest1 + job_notice1[0].get('href')
        bot.sendMessage(chat_id=chat_id, text=text)
        with open(os.path.join(BASE_DIR, 'job_latest1.txt'), 'w+') as f:
            f.write(job_latest1)
    else:
        pass

with open(os.path.join(BASE_DIR, 'job_latest2.txt'), 'r+') as f_read:
    before = f_read.read()
    if before != job_latest2:
        text = menu[0].text + job_latest2.replace("					", "") + job_notice2[0].get('href')
        bot.sendMessage(chat_id=chat_id, text=text)
        with open(os.path.join(BASE_DIR, 'job_latest2.txt'), 'w+') as f:
            f.write(job_latest2)
    else:
        pass
