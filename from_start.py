from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import random
import os
current_directory= os.path.dirname(os.path.realpath(__file__))
path = current_directory
os.chdir(path)

with open(path + '/answers.txt') as f:
    lines = f.read().splitlines()
updater = Updater(token='535090351:AAFzQDZ3osy5oUaCxTViR9seLsL6jBu214o') # Токен API к Telegram
dispatcher = updater.dispatcher
# Обработка команд
def startCommand(bot, update):
    bot.send_message(chat_id=update.message.chat_id, text='Привет, давай пообщаемся?')
def textMessage(bot, update):
    # bot.send_message(chat_id=update.message.chat_id, text='думаю')

    response = random.choice(lines)
    logger(update)
    if update.message.text == 'тест':
        bot.send_message(chat_id=update.message.chat_id, text='Потестируй себя, умник!')
    elif update.message.text[0] == 'х':
        bot.send_photo(chat_id=update.message.chat_id, photo=open(path + random.choice(['/dog.jpeg' ,'/kitty.jpeg']), 'rb'))
    else :
        bot.send_message(chat_id=update.message.chat_id, text=response)
def logger(mess):


    file =  open(path + '/qu.txt', 'a')
    file.write(str(mess.message.chat) + '    ' + mess.message.text + '\n')
    file.close()


start_command_handler = CommandHandler('start', startCommand)
text_message_handler = MessageHandler(Filters.text, textMessage)
# Добавляем хендлеры в диспетчер
dispatcher.add_handler(start_command_handler)
dispatcher.add_handler(text_message_handler)
# Начинаем поиск обновлений
updater.start_polling(clean=True)
# Останавливаем бота, если были нажаты Ctrl + C
updater.idle()
