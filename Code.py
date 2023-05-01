import os
import psutil
import telebot
bot = telebot.TeleBot('TOKEN')
GAMES = ["program_1", "program_2", "program_3"]
def check_games():
    out=[]
    for i in psutil.pids():
        try:
            p = psutil.Process(i)
        except psutil.NoSuchProcess:
            continue
        if p.name() in GAMES:
            out.append(p.name())
    return out
result = check_games()
print(result)
@bot.message_handler(commands=['start', 'hello'])
def send_welcome(message):
    print('hello')
    bot.reply_to(message.chat.id, "Howdy, how are you doing?")
@bot.message_handler(func=lambda msg: True)
def echo_all(message):
    print('hello')
    bot.reply_to(message.chat.id, message.text)
bot.infinity_polling()
#bot.polling(none_stop=True, interval=0)
cmd='tasklist>list_of_the_processes.txt'
code_exit=os.system(cmd)
print(code_exit)