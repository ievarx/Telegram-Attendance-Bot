from telegram import InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Updater, CommandHandler, CallbackQueryHandler
import mysql.connector
from datetime import datetime

# Replace these values with your bot token and database credentials
TOKEN = 'bot token '
DB_HOST = 'localhost'
DB_USER = 'root'
DB_PASS = ''
DB_NAME = 'telebot'

db = mysql.connector.connect(
    host=DB_HOST,
    user=DB_USER,
    password=DB_PASS,
    database=DB_NAME
)
cursor = db.cursor()

def start(update, context):
    cursor.execute("SELECT name FROM students")
    students = cursor.fetchall()
    context.user_data['students'] = students
    context.user_data['index'] = 0
    context.user_data['attendances'] = {}
    show_next_student(update, context)

def show_next_student(update, context):
    students = context.user_data['students']
    index = context.user_data['index']
    if index < len(students):
        student = students[index][0]
        keyboard = [[InlineKeyboardButton("حاضر", callback_data=f"present_{student}"),
                     InlineKeyboardButton("غائب", callback_data=f"absent_{student}")]]
        reply_markup = InlineKeyboardMarkup(keyboard)
        if update.message:
            update.message.reply_text(f"الطالب: {student}", reply_markup=reply_markup)
        else:
            context.bot.send_message(chat_id=update.callback_query.message.chat_id, text=f"الطالب: {student}", reply_markup=reply_markup)
    else:
        save_attendance(context)
        context.bot.send_message(chat_id=update.callback_query.message.chat_id, text="تمت عملية التسجيل لجميع الطلاب.")

def button(update, context):
    query = update.callback_query
    action, student = query.data.split('_')
    context.user_data['attendances'][student] = action
    context.user_data['index'] += 1
    show_next_student(update, context)

def save_attendance(context):
    today_date = datetime.today().strftime('%Y-%m-%d')
    for student, status in context.user_data['attendances'].items():
        cursor.execute("INSERT INTO attendance (student_name, status, date) VALUES (%s, %s, %s)", (student, status, today_date))
    db.commit()

updater = Updater(token=TOKEN, use_context=True)
dispatcher = updater.dispatcher
dispatcher.add_handler(CommandHandler('start', start))
dispatcher.add_handler(CallbackQueryHandler(button))

updater.start_polling()
updater.idle()
