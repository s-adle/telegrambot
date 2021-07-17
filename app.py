from telegram.ext import Updater, MessageHandler, Filters
def demo1(bot,update):
   bot.message.reply_text('I am fine')
def demo2(bot,update):
   bot.message.reply_text('My name is sadle-bot')
def main(bot,update):
  a=bot.message.text.lower()
  print(a)
  if a=="how are you?":
    demo1(bot,update)
  elif a=="what is your name?" or a=="name please":
    demo2(bot,update)
  else :
    bot.message.reply_text('invalid text')
BOT_TOKEN = '1936488577:AAFSC83Z99TDDOZuG8g65fC6pOEfUElXkI0'
u= Updater(BOT_TOKEN,use_context=True)
dp=u.dispatcher
dp.add_handler(MessageHandler(Filters.text,main))
u.start_polling()
u.idle()
