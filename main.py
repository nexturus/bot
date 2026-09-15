import telebot
import random
bot = telebot.TeleBot("8688957649:AAG4LJdT-HdE4dtpfgqPO5iiCfL2Y-UHR_I")

guesses = {

}

@bot.message_handler(commands=["start"])
def start(message:telebot.types.Message):
    bot.send_message(chat_id=message.chat.id, text="Вас выбрали для отбора самых везучих людей на планете! Для такого случая, мы загадали число от 1 до 10. Попробуйте отгадать.")
    guesses[message.chat.username] = str(random.randint(1,10))

@bot.message_handler(content_types=["text"])
def send(message:telebot.types.Message):
    if message == guesses[message.chat.username]:
        bot.send_message(chat_id=message.chat.id, text="Вы угадали! С вами скоро свяжутся.", reply_to_message_id=message.id)
        guesses.pop(message.chat.username)
    else:
        bot.send_message(chat_id=message.chat.id, text="Неверно. Попытайте удачу ещё раз.", reply_to_message_id=message.id)
        guesses[message.chat.username] = str(random.randint(1, 10))

bot.infinity_polling()