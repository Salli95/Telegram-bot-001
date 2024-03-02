
# TOKEN = '6255065745:AAHpLskHG978WYcSJtXhbderZsC2hr7CqHU'
import telebot
import random
import time
import threading

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
    bot.send_message(message.chat.id, "Записал твой ID, жди поздравлений")
    print("Received message:", message.text)

# Функция для отправки сообщения каждому пользователю из списка
def send_messages():
    while True:
        print("Sending messages to users...")
        for user_id in user_ids:
            message = random.choice(wishes)
            print("Sending message to user", user_id, ":", message)  # Отладочная информация
            bot.send_message(user_id, message)
            time.sleep(1)  # Задержка, чтобы не превысить лимиты API
        print("All messages sent.")
        time.sleep(60)  # Пауза в 60 секунд

# Запускаем функцию отправки сообщений в отдельном потоке, если она еще не запущена
if 'thread_send' not in locals() or not thread_send.is_alive():
    thread_send = threading.Thread(target=send_messages)
    thread_send.start()

# Запускаем бота в отдельном потоке
print("Starting bot polling...")
bot.polling(none_stop=True)
