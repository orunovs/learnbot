from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import logging
import setings

logging.basicConfig(format='%(asctime)s - %(levelname)s - %(message)s -%(name)s',
                    level=logging.INFO,
                    filename='bot.log'
                    )




def greet_user(update, bot):
    text = 'Вызван/ start'
    logging.info(text)
    update.message.reply_text(text)


def talk_to_me(update, bot):
   user_text = update.message.text
   print(f'Тебя зовут: {update.message.chat.first_name} и ты написал: {update.message.text}')
   logging.info("User %s, Chat id: %s, Message: %s", update.message.chat.username,
                update.message.chat_id, update.message.text)
   update.message.reply_text(user_text)


def main():
    mybot = Updater(setings.API_KEY)

    db = mybot.dispatcher
    db.add_handler(CommandHandler('start', greet_user))
    db.add_handler(MessageHandler(Filters.text, talk_to_me))

    mybot.start_polling()
    mybot.idle()


main()