import telebot
from bot_logic import gen_pass
import random
import time, threading, schedule    
bot = telebot.TeleBot("7440348278:AAEvzwgiuoHSTwCWk-0KAgGKE28t-pnkjr0")
    
@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "Привет, я бот который ставит таймер на чай ееее")
    

@bot.message_handler(commands=['hello'])
def send_hello(message):
    bot.reply_to(message, "Поздоровались уже брух")

@bot.message_handler(commands=['bye'])
def send_bye(message):
    bot.reply_to(message, "давай давай иди чай пить")




bot.delete_my_commands(scope=None, language_code=None)

bot.set_my_commands(
    commands=[
        telebot.types.BotCommand("set", "'чай поставьте' ахх таймер"),
        telebot.types.BotCommand("unset", "убери таймер >:<")
    ],
    
)

# check command
cmd = bot.get_my_commands(scope=None, language_code=None)
print([c.to_json() for c in cmd])


def beep(chat_id) -> None:
    """Send the beep message."""
    bot.send_message(chat_id, text='бибип йоу')


@bot.message_handler(commands=['set'])
def set_timer(message):
    args = message.text.split()
    if len(args) > 1 and args[1].isdigit():
        sec = int(args[1])
        schedule.every(sec).seconds.do(beep, message.chat.id).tag(message.chat.id)
    else:
        bot.reply_to(message, 'делай так: /set <секунды> (тип на скок сек хочш поставить)')


@bot.message_handler(commands=['unset'])
def unset_timer(message):
    schedule.clear(message.chat.id)


if __name__ == '__main__':
    threading.Thread(target=bot.infinity_polling, name='bot_infinity_polling', daemon=True).start()
    while True:
        schedule.run_pending()
        time.sleep(1)




bot.polling()
