from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup

from telegram.ext import Updater, CommandHandler, CallbackQueryHandler, CallbackContext


# داده‌های کتاب‌ها و سوالات

books = {

    "adventure": {

        "title": "عادت های اتمی",

        "author": "جیمز کلیر",

        "image_url": "https://nashrenovin.ir/wp-content/uploads/2019/04/Atomic-Habits.webp"

    },

    "money": {

        "title": "دفترچه یادداشت",

        "author": "نیکولاس اسپارک",

 # اینجا URL تصویر را وارد کنید

    }

}


questions = {

    "question1": {

        "text": "چه موضوعی شما را بیشتر جذب می‌کند؟",

        "options": [

            {"text": "هیجان و ماجراجویی", "value": "adventure"},

            {"text": "انگیزشی پول و ثروت", "value": "money"},

        ]

    }

}


# تابع برای شروع ربات

def start(update: Update, context: CallbackContext) -> None:

    print("کد درحال اجراست")

    keyboard = [[InlineKeyboardButton(option['text'], callback_data=option['value'])] for option in questions['question1']['options']]

    reply_markup = InlineKeyboardMarkup(keyboard)

    update.message.reply_text(questions['question1']['text'], reply_markup=reply_markup)


# تابع برای پردازش پاسخ‌ها

def button(update: Update, context: CallbackContext) -> None:

    query = update.callback_query

    query.answer()
    

    book_key = query.data

    if book_key in books:

        book = books[book_key]

        response_text = f"کتاب مناسب شما:\n\nعنوان: {book['title']}\nنویسنده: {book['author']}\nتصویر: {book['image_url']}"

        query.edit_message_text(text=response_text)
    else:

        query.edit_message_text(text="پاسخ نامعتبر")


# تنظیمات و راه‌اندازی ربات

def main():
   
    TOKEN = ""

    updater = Updater(TOKEN)


    updater.dispatcher.add_handler(CommandHandler("start", start))

    updater.dispatcher.add_handler(CallbackQueryHandler(button))


    updater.start_polling()

    updater.idle()


if __name__ == '__main__':

    main()

