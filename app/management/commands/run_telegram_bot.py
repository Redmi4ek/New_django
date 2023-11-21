from django.core.management.base import BaseCommand
import telebot 
from app.models import News
import datetime


bot = telebot.TeleBot("6945373166:AAEqSmGnHaP_IXmaM_K8J-dcMympkEEzBic") 

# user_data = {}


@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, "Hello world!")

@bot.message_handler(commands=['newes'])
def Newes(message):
    news = News.objects.all()
    for news in news:
        bot.send_message(message.chat.id, news.public)
        bot.send_message(message.chat.id, news.date)

@bot.message_handler(commands=['help'])
def help(message):
    available_commands = [
        "/start - Начало взаимодействия ",
        "/newes - Показывает новости и данные",
        "/help - Показывает список доступных команд ",
        "/add - ВАЖНО! пишите все по данной формуле , с начала '/add' [новость] [дата в формате гггг-мм-дд(тире обязательно)] "
    ]
    bot.send_message(message.chat.id,"available_commands:\n\n" )
    for command in available_commands:
        bot.send_message(message.chat.id, command)

@bot.message_handler(func=lambda message: message.text.startswith('/add'), content_types=['text'])
def handle_add_command(message):
    chat_id = message.chat.id

    try:
        # Разбиваем введенные данные
        _, news, date_str = message.text.split(' ', 2)

        # Преобразуем строку даты в объект datetime
        date = datetime.datetime.strptime(date_str, '%Y-%m-%d').date()

        # Сохраняем данные в модели Django
        news_entry = News(public=news, date=date)
        news_entry.save()

        # Отправляем подтверждение пользователю
        bot.send_message(chat_id, "Новость успешно добавлена в базу данных!")
    except ValueError:
        # Обработка ошибок, например, если введенные данные не соответствуют ожидаемому формату
        bot.send_message(chat_id, "Ошибка в формате данных. Пожалуйста, введите данные в правильном формате.")




@bot.message_handler(func=lambda message: True)
def echo_all(message):
    bot.reply_to(message, message.text)


    

class Command(BaseCommand):
    def handle(self, *args, **options): 
        print("Starting bot...") 
        bot.polling()
        print("Bot creeping")  
