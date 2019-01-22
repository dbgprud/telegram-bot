import telegram
from telegram.ext import Updater, CommandHandler
import requests
from bs4 import BeautifulSoup
import os

my_token = '645804650:AAEFzjMH_sL6fU3oj-k12pCsLexAw8Uyzjs'
bot = telegram.Bot(token=my_token)
updates = bot.getUpdates()
chat_id = "702266940"
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

def start(bot,update):
    with open(os.path.join(BASE_DIR, 'hello.txt'), 'r+') as f_read:
        hello = f_read.read()
        bot.sendMessage(chat_id=chat_id, text=hello)

def depart(bot, update):
    depart_notice = requests.get('http://computer.cnu.ac.kr/index.php?mid=notice')
    depart_notice.encoding = 'utf-8'
    depart_html = depart_notice.text
    depart_soup = BeautifulSoup(depart_html, 'html.parser')
    update.message.reply_text("depart")
    a = ""
    for text in depart_soup.select("tr.notice > td.title > a"):
        a = a + "\n" + text.text +"\n"+ text.get('href')
    for no in depart_soup.select("td.title > a.hx"):
        a = a + no.text.replace("					", "")+"\n"+ text.get('href')
    bot.sendMessage(chat_id=chat_id,text=a)

    with open(os.path.join(BASE_DIR, 'hello.txt'), 'r+') as f_read:
        hello = f_read.read()
        bot.sendMessage(chat_id=chat_id, text=hello)

def com(bot, update):
    com_notice = requests.get('http://computer.cnu.ac.kr/index.php?mid=gnotice')
    com_notice.encoding = 'utf-8'
    com_html = com_notice.text
    com_soup = BeautifulSoup(com_html, 'html.parser')
    update.message.reply_text("com")
    a = ""
    for text in com_soup.select("tr.notice >td.title > a"):
        a = a + "\n" + text.text+"\n"+ text.get('href')
    for no in com_soup.select("td.title > a.hx"):
        a = a + no.text.replace("					", "")+"\n"+ text.get('href')
    bot.sendMessage(chat_id=chat_id,text=a)

    with open(os.path.join(BASE_DIR, 'hello.txt'), 'r+') as f_read:
        hello = f_read.read()
        bot.sendMessage(chat_id=chat_id, text=hello)

def sa(bot, update):
    sa_notice = requests.get('http://computer.cnu.ac.kr/index.php?mid=saccord')
    sa_notice.encoding = 'utf-8'
    sa_html = sa_notice.text
    sa_soup = BeautifulSoup(sa_html, 'html.parser')
    update.message.reply_text("sa")
    a = ""
    for text in sa_soup.select("tr.notice >td.title > a"):
        a = a + "\n" + text.text+"\n"+ text.get('href')
    for no in sa_soup.select("td.title > a.hx"):
        a = a + no.text.replace("					", "")+"\n"+ text.get('href')
    bot.sendMessage(chat_id=chat_id,text=a)

    with open(os.path.join(BASE_DIR, 'hello.txt'), 'r+') as f_read:
        hello = f_read.read()
        bot.sendMessage(chat_id=chat_id, text=hello)

def job(bot, update):
    job_notice = requests.get('http://computer.cnu.ac.kr/index.php?mid=job')
    job_notice.encoding = 'utf-8'
    job_html = job_notice.text
    job_soup = BeautifulSoup(job_html, 'html.parser')
    update.message.reply_text("job")
    a = ""
    for text in job_soup.select("tr.notice >td.title > a"):
        a = a + "\n" + text.text+"\n"+ text.get('href')
    for no in job_soup.select("td.title > a.hx"):
        a = a + no.text.replace("					", "")+"\n"+ text.get('href')
    bot.sendMessage(chat_id=chat_id,text=a)

    with open(os.path.join(BASE_DIR, 'hello.txt'), 'r+') as f_read:
        hello = f_read.read()
        bot.sendMessage(chat_id=chat_id, text=hello)

updater = Updater(my_token)
dp = updater.dispatcher
dp.add_handler(CommandHandler('start', start))
dp.add_handler(CommandHandler('depart', depart))
dp.add_handler(CommandHandler('com', com))
dp.add_handler(CommandHandler('sa', sa))
dp.add_handler(CommandHandler('job', job))
updater.start_polling(timeout=1, clean=True)
updater.idle()
