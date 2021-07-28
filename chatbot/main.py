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
        fr'안녕😺 {user.mention_markdown_v2()} 나는 뉴스캣이다냥 궁금한게 있다면, /help를 쳐봐라냥\!',
        reply_markup=ForceReply(selective=True),
    )

def selectcat(update: Update, context: CallbackContext) -> int:
    user = update.message.from_user
    logger.info("고객님의 선호 카테고리 %s: %s", user.id, update.message.text)
    update.message.reply_text(
        '오케이 카테고리 선정 완료 \n \
        이제, /news 를 쳐봐라냥. 너를 위한 뉴스가 준비되어있다냥',
    )
    nobody = squery.Userquery(User_id = user.id, pref = update.message.text)
    nobody.querrytords()



def send_news(update: Update, context: CallbackContext) -> None:
    user = update.message.from_user
    send_rco = squery.Userquery(User_id = user.id, pref = update.message.text)
    update.message.reply_text('너를 위해 준비했다냥😼\n\n\
    맘에 들었던 기사가 있었다면,\n\n \
    /like 기사 번호\
    [ex /like 3 2 5]\n\n \
    를 적어라냥🐱\n\n\
    ✔ 1번째 뉴스\n {} \n\n \
    ✔ 2번째 뉴스\n {} \n\n \
    ✔ 3번째 뉴스\n {} \n\n \
    ✔ 4번째 뉴스\n {} \n\n \
    ✔ 5번째 뉴스\n {} \n\n \
     '.format(send_rco.send_reco()[0],send_rco.send_reco()[1],
                                        send_rco.send_reco()[2], send_rco.send_reco()[3],
                                        send_rco.send_reco()[4]) ## 리스트 컴프리헨션 가능할지도!
    )
    print(user.id)


def help_command(update: Update, context: CallbackContext) -> None:
    update.message.reply_text('뉴스캣 정보 알림\n\n\
    /view_cat : 뉴스 카테고리 확인\
    \n\n/select_cat : 뉴스카테고리 선택\n\n/help : 핼프 커맨드\n\n/news : 추천 뉴스보기\n\n/funding : 뉴스캣 후원하기 ')


## 신규 기능
def like_log(update: Update, context: CallbackContext) -> None:
    user = update.message.from_user
    logger.info("선호 뉴스 번호 %s: %s", user.id, update.message.text)
    send_rco = squery.Userquery(User_id = user.id, pref = update.message.text)
    send_rco.send_like()
    update.message.reply_text('옷케 ~ 접수했어냥😎')
    

## 신규 기능

def view_cat(update: Update, context: CallbackContext) -> None:
    update.message.reply_text('아래 뉴스 카테고리에서, \
        2가지를 구독할 수 있다냥🐱.\
         \n\n  정치, 경제, 사회, 국제, 스포츠 \n\n\n 카테고리를 골랐다면, \n\n\n \
         /select_cat 카테고리1, 카테고리2 를 입력해줘냥' )


def echo(update: Update, context: CallbackContext) -> None:
    update.message.reply_text(update.message.text)


def funding(update: Update, context: CallbackContext) -> None:
    update.message.reply_text('❤뉴스캣 후원계좌❤ \
         \n\n  카카오뱅크 최윤석 1331-324-23541 \n\n\n  \
         여러분의 후원액은 뉴스캣의 사료비로 충당된다냥😼' )

def unknown(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text="뭔 🐶소리냥")


def main() -> None:

    updater = Updater("1909634364:AAEqg6352ES9y1XmsaaoopFdqItNjpHKTSk")


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

