import telebot
import random
import time
import threading
import schedule
from goodmorning import wishes
from background import keep_alive 

TOKEN = '6255065745:AAHpLskHG978WYcSJtXhbderZsC2hr7CqHU'

bot = telebot.TeleBot(TOKEN)

# Список ID пользователей, которым нужно отправить сообщения
user_ids = set()  

@bot.message_handler(func=lambda message: True)
def handle_message(message):
    # Добавляем ID отправителя в список пользователей
    user_ids.add(message.chat.id)
    bot.send_message(message.chat.id, f"Записал твой ID: {message.chat.id}")
    bot.send_message(message.chat.id, "Жди доброе утро от Salli95 каждую минуту")
    print(user_ids)
    print("Received message:", message.text)


# Функция для отправки сообщения
def send_message():
    message = random.choice(wishes)
    for user_id in user_ids:
        bot.send_message(user_id, message)
        print("Пожелание:", message)
      

# Планирование отправки сообщений каждый день в 7:00
# schedule.every().day.at("22:38").do(send_message)
schedule.every().minute.do(send_message)


# Запускаем бота в отдельном потоке
print("Starting bot polling...")
thread_bot = threading.Thread(target=bot.polling, kwargs={'none_stop': True})
thread_bot.start()

keep_alive()#запускаем flask-сервер в отдельном потоке. 

# Запускаем планировщик в отдельном потоке
while True:
    schedule.run_pending()
    time.sleep(1)
