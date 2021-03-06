import logging
from telegram import ForceReply ,ReplyKeyboardRemove, Update, ReplyKeyboardMarkup
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext, ConversationHandler


import pandas as pd 
import pymysql as sql

from sqlquery import squery


logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO
)

logger = logging.getLogger(__name__)


def start(update: Update, context: CallbackContext) -> None:
    user = update.effective_user
    update.message.reply_markdown_v2(
        fr'์๋๐บ {user.mention_markdown_v2()} ๋๋ ๋ด์ค์บฃ์ด๋ค๋ฅ ๊ถ๊ธํ๊ฒ ์๋ค๋ฉด, /help๋ฅผ ์ณ๋ด๋ผ๋ฅ\!',
        reply_markup=ForceReply(selective=True),
    )

def selectcat(update: Update, context: CallbackContext) -> int:
    user = update.message.from_user
    logger.info("๊ณ ๊ฐ๋์ ์ ํธ ์นดํ๊ณ ๋ฆฌ %s: %s", user.id, update.message.text)
    update.message.reply_text(
        '์ค์ผ์ด ์นดํ๊ณ ๋ฆฌ ์ ์  ์๋ฃ \n \
        ์ด์ , /news ๋ฅผ ์ณ๋ด๋ผ๋ฅ. ๋๋ฅผ ์ํ ๋ด์ค๊ฐ ์ค๋น๋์ด์๋ค๋ฅ',
    )
    nobody = squery.Userquery(User_id = user.id, pref = update.message.text)
    nobody.querrytords()



def send_news(update: Update, context: CallbackContext) -> None:
    user = update.message.from_user
    send_rco = squery.Userquery(User_id = user.id, pref = update.message.text)
    update.message.reply_text('๋๋ฅผ ์ํด ์ค๋นํ๋ค๋ฅ๐ผ\n\n\
    ๋ง์ ๋ค์๋ ๊ธฐ์ฌ๊ฐ ์์๋ค๋ฉด,\n\n \
    /like ๊ธฐ์ฌ ๋ฒํธ\
    [ex /like 3 2 5]\n\n \
    ๋ฅผ ์ ์ด๋ผ๋ฅ๐ฑ\n\n\
    โ 1๋ฒ์งธ ๋ด์ค\n {} \n\n \
    โ 2๋ฒ์งธ ๋ด์ค\n {} \n\n \
    โ 3๋ฒ์งธ ๋ด์ค\n {} \n\n \
    โ 4๋ฒ์งธ ๋ด์ค\n {} \n\n \
    โ 5๋ฒ์งธ ๋ด์ค\n {} \n\n \
     '.format(send_rco.send_reco()[0],send_rco.send_reco()[1],
                                        send_rco.send_reco()[2], send_rco.send_reco()[3],
                                        send_rco.send_reco()[4]) ## ๋ฆฌ์คํธ ์ปดํ๋ฆฌํจ์ ๊ฐ๋ฅํ ์ง๋!
    )
    print(user.id)


def help_command(update: Update, context: CallbackContext) -> None:
    update.message.reply_text('๋ด์ค์บฃ ์ ๋ณด ์๋ฆผ\n\n\
    /view_cat : ๋ด์ค ์นดํ๊ณ ๋ฆฌ ํ์ธ\
    \n\n/select_cat : ๋ด์ค์นดํ๊ณ ๋ฆฌ ์ ํ\n\n/help : ํผํ ์ปค๋งจ๋\n\n/news : ์ถ์ฒ ๋ด์ค๋ณด๊ธฐ\n\n/funding : ๋ด์ค์บฃ ํ์ํ๊ธฐ ')


## ์ ๊ท ๊ธฐ๋ฅ
def like_log(update: Update, context: CallbackContext) -> None:
    user = update.message.from_user
    logger.info("์ ํธ ๋ด์ค ๋ฒํธ %s: %s", user.id, update.message.text)
    send_rco = squery.Userquery(User_id = user.id, pref = update.message.text)
    send_rco.send_like()
    update.message.reply_text('์ท์ผ ~ ์ ์ํ์ด๋ฅ๐')
    

## ์ ๊ท ๊ธฐ๋ฅ

def view_cat(update: Update, context: CallbackContext) -> None:
    update.message.reply_text('์๋ ๋ด์ค ์นดํ๊ณ ๋ฆฌ์์, \
        2๊ฐ์ง๋ฅผ ๊ตฌ๋ํ  ์ ์๋ค๋ฅ๐ฑ.\
         \n\n  ์ ์น, ๊ฒฝ์ , ์ฌํ, ๊ตญ์ , ์คํฌ์ธ  \n\n\n ์นดํ๊ณ ๋ฆฌ๋ฅผ ๊ณจ๋๋ค๋ฉด, \n\n\n \
         /select_cat ์นดํ๊ณ ๋ฆฌ1, ์นดํ๊ณ ๋ฆฌ2 ๋ฅผ ์๋ ฅํด์ค๋ฅ' )


def echo(update: Update, context: CallbackContext) -> None:
    update.message.reply_text(update.message.text)


def funding(update: Update, context: CallbackContext) -> None:
    update.message.reply_text('โค๋ด์ค์บฃ ํ์๊ณ์ขโค \
         \n\n  ์นด์นด์ค๋ฑํฌ ์ต์ค์ 1331-324-23541 \n\n\n  \
         ์ฌ๋ฌ๋ถ์ ํ์์ก์ ๋ด์ค์บฃ์ ์ฌ๋ฃ๋น๋ก ์ถฉ๋น๋๋ค๋ฅ๐ผ' )

def unknown(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text="๋ญ ๐ถ์๋ฆฌ๋ฅ")

### Plz Put your chabot information #######
def main() -> None:

    updater = Updater("chatbot")


    dispatcher = updater.dispatcher

    dispatcher.add_handler(CommandHandler("start", start))
    dispatcher.add_handler(CommandHandler("help", help_command))
    dispatcher.add_handler(CommandHandler("view_cat", view_cat))
    dispatcher.add_handler(CommandHandler("select_cat", selectcat))
    dispatcher.add_handler(CommandHandler("funding", funding))
    dispatcher.add_handler(CommandHandler("news", send_news))
    dispatcher.add_handler(CommandHandler("like", like_log))

  
    dispatcher.add_handler(MessageHandler(Filters.text & ~Filters.command, echo))


    unknown_handler = MessageHandler(Filters.command, unknown)
    dispatcher.add_handler(unknown_handler)

  
    updater.start_polling()
    # updater.stop()


    updater.idle()


if __name__ == '__main__':
    main()

