
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import DBoperator

def start(bot, update):
    update.message.reply_text('Hello! This is Party-Time.Bot. You can use one of the commands present in the interface:')
    update.message.reply_text('/start')
    update.message.reply_text('/playlist')
    update.message.reply_text('/all_songs')
    update.message.reply_text('/vote_next')
def echo(bot, update):
    bot.send_message(chat_id=update.message.chat_id, text=update.message.text)
    print(update.message.text)
def unknown(bot, update):
    bot.send_message(chat_id=update.message.chat_id, text="Sorry, I didn't understand that command.")
def playlist(bot, update):
    update.message.reply_text('playlist')
def all_songs(bot, update):
    print(DBoperator.showAllMusic())
    update.message.reply_text('all')
def vote_next(bot, update):
    update.message.reply_text('next')

if __name__ == '__main__':

    # main program
    updater = Updater(token='572398012:AAE0qyUkJn15oX37JzbdWDLMIm5uhCKs88U')

    # add an handler to start the bot replying with the list of available commands
    dispatcher = updater.dispatcher
    dispatcher.add_handler(CommandHandler('start', start))

    dispatcher = updater.dispatcher
    dispatcher.add_handler(CommandHandler('playlist', playlist))

    dispatcher = updater.dispatcher
    dispatcher.add_handler(CommandHandler('all_songs', all_songs))

    dispatcher = updater.dispatcher
    dispatcher.add_handler(CommandHandler('vote_next', vote_next))

    #add at bottom not before other dispatcher
    echo_handler = MessageHandler(Filters.text, echo)
    dispatcher.add_handler(echo_handler)
    unknown_handler = MessageHandler(Filters.command, unknown)
    dispatcher.add_handler(unknown_handler)
    updater.start_polling()
    updater.idle()