import telebot
import random
import time
import threading
import schedule
from goodmorning import wishes


TOKEN = '6255065745:AAHpLskHG978WYcSJtXhbderZsC2hr7CqHU'

bot = telebot.TeleBot(TOKEN)

# Функция для сохранения ID пользователей в файл
def save_user_ids(user_ids):
    with open("user_ids.txt", "w") as file:
        for user_id in user_ids:
            file.write(str(user_id) + "\n")

# Функция для чтения ID пользователей из файла
def load_user_ids():
    user_ids = set()
    try:
        with open("user_ids.txt", "r") as file:
            for line in file:
                user_ids.add(int(line.strip()))
    except FileNotFoundError:
        pass
    return user_ids

# Список ID пользователей, которым нужно отправить сообщения
user_ids = load_user_ids()

@bot.message_handler(func=lambda message: True)
def handle_message(message):
    # Добавляем ID отправителя в список пользователей
    user_ids.add(message.chat.id)
    save_user_ids(user_ids)
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
      

# Планирование отправки сообщений каждую минуту (замените на необходимое время)
schedule.every().minute.do(send_message)

# Запускаем бота в отдельном потоке
print("Starting bot polling...")
thread_bot = threading.Thread(target=bot.polling, kwargs={'none_stop': True})
thread_bot.start()

# Запускаем планировщик в отдельном потоке
while True:
    schedule.run_pending()
    time.sleep(1)
