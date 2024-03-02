
# TOKEN = '6255065745:AAHpLskHG978WYcSJtXhbderZsC2hr7CqHU'
import telebot
import random
import time
import threading
import schedule

# Токен вашего бота
TOKEN = '6255065745:AAHpLskHG978WYcSJtXhbderZsC2hr7CqHU'

# Создаем бота
bot = telebot.TeleBot(TOKEN)

# Сообщения-поздравления
wishes = [
    "Привет, моя маленькая пингвиниха! Пусть тепло любви согревает тебя в этот день.",
    "Доброе утро, моя маленькая бегемотиха! Пусть твой день будет ярким и радостным!",
    "Привет, моя маленькая белочка! Не забудь пополнить запас знаний на сегодняшний день.",
    "Доброе утро, моя маленькая единорожка! Пусть твои мечты сбываются сегодня и всегда!",
    "Привет, моя маленькая пандочка! Улыбнись, и пусть этот день будет прекрасным для всех."
]

# Список ID пользователей, которым нужно отправить сообщения
user_ids = set()  # Множество для уникальных ID пользователей

# Обработчик входящих сообщений
@bot.message_handler(func=lambda message: True)
def handle_message(message):
    # Добавляем ID отправителя в список пользователей
    user_ids.add(message.chat.id)
    bot.send_message(message.chat.id, "Записал твой ID, жди поздравлений 010")
    print("Received message:", message.text)

# Функция для отправки сообщения
def send_message():
    message = random.choice(wishes)
    for user_id in user_ids:
        bot.send_message(user_id, message)

# Планирование отправки сообщений каждый день в 7:00
schedule.every().day.at("20:46").do(send_message)

# Запускаем бота в отдельном потоке
print("Starting bot polling...")
thread_bot = threading.Thread(target=bot.polling, kwargs={'none_stop': True})
thread_bot.start()

# Запускаем планировщик в отдельном потоке
while True:
    schedule.run_pending()
    time.sleep(1)
