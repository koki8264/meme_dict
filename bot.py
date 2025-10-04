import telebot
from bot_logic import gen_pass
import random
import time, threading, schedule    
bot = telebot.TeleBot("7440348278:AAEvzwgiuoHSTwCWk-0KAgGKE28t-pnkjr0")
    
@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "Привет! Я твой Telegram бот. Напиши что-нибудь!")
    

@bot.message_handler(commands=['hello'])
def send_hello(message):
    bot.reply_to(message, "Привет! Как дела?")

@bot.message_handler(commands=['bye'])
def send_bye(message):
    bot.reply_to(message, "Пока! Удачи!")


# @bot.message_handler(func=lambda message: True)
# def echo_all(message):
#     if message.text == 'пароль':
#         bot.reply_to(message, gen_pass(10))
#     else:
#         bot.reply_to(message, message.text)

bot.delete_my_commands(scope=None, language_code=None)

bot.set_my_commands(
    commands=[
        telebot.types.BotCommand("set", "'чай поставьте' ахх таймер"),
        telebot.types.BotCommand("unset", "убери таймер >:<")
    ],
    # scope=telebot.types.BotCommandScopeChat(12345678)  # use for personal command for users
    # scope=telebot.types.BotCommandScopeAllPrivateChats()  # use for all private chats
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


@bot.message_handler(commands=['coin'])
def send_coin(message):
    result = random.choice(["орел", "решка"])
    bot.reply_to(message, result)

bot.polling()