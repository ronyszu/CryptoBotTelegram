from telegram import Update
from telegram.ext import CallbackContext
from telegram.ext import CommandHandler
from telegram.ext import Updater

import datanews
datanews.api_key = '0mvs62wkhvjbwbqd0cv31kz8z'



def start(update: Update, context: CallbackContext):
    context.bot.send_message(chat_id=update.effective_chat.id, text="Seja bem vindo ao Bot CryptoNews desenvolvido por Rony Szuster. Para pesquisar notícias, entre: /search <termo>")
    
def _fetch_data(update, context, fetcher):
  if not context.args:
    return update.message.reply_text('Favor inserir um termo para a pesquisa.')

  query = '"' + ' '.join(context.args) + '"'
  result = fetcher(query)

  if not result['hits']:
    update.message.reply_text('Desculpe, sua pesquisa não funcionou corretamente ou não retornou resultado algum.')
    return

  last_message = update.message
  for article in reversed(result['hits']):
    text = article['title'] + ': ' + article['url']
    last_message = last_message.reply_text(text)

def search_command(update, context):
  def fetcher(query):
    return datanews.headlines(query, size=10, sortBy='date', page=0, language='en')
  _fetch_data(update, context, fetcher)


updater = Updater(token='5058509223:AAHGqtz7M2J_zuI7-PNLA46-TdqFp4Eapls', use_context=True)
updater.start_polling()
dispatcher = updater.dispatcher
dispatcher.add_handler(CommandHandler('search', search_command))
start_handler = CommandHandler('start', start)
dispatcher.add_handler(start_handler)




