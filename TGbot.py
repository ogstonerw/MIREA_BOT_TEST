import telebot
from telebot import types
bot = telebot.TeleBot('5662293194:AAG7BXMeFt7VD4BeC021G8SnNp0-eIqIFSY')

@bot.message_handler(commands=['start'])
def start(message):
    markup = types.InlineKeyboardMarkup()
    button_site = types.InlineKeyboardButton("Сайт РТУ МИРЭА", url='https://www.mirea.ru/')
    button_shop = types.InlineKeyboardButton("Интернет-магазин", url='https://www.google.com/')  # Замените на реальный URL вашего интернет-магазина
    markup.add(button_site, button_shop)


    bot.send_message(message.chat.id, "Привет, {0.first_name}! Это бот РТУ МИРЭА)".format(message.from_user), reply_markup=markup)

# Запуск бота
if __name__ == "__main__":
    bot.polling(none_stop=True)
