from random import randint
import telebot

# Connecting to the Telegram bot with the bot token.
bot = telebot.TeleBot('YOUR-TOKEN')
random_number = randint(0, 100)

# Send the message when it is sent in the /start robot.
@bot.message_handler(commands=['start'])
def start(message):
    bot.reply_to(message, "Welcome to the Number Guessing Game! I'm thinking of a number between 0 and 100. Take a guess!")

# Send your message by bot.
@bot.message_handler(func=lambda message: True)
def game(message):
    """
    Personal codes.
    """
    try:
        input_user = int(message.text)
        if input_user < 0 or input_user > 100:
            raise ValueError
    except ValueError:
        bot.reply_to(message, "Please enter a number between 0 and 100.")
    else:
        if input_user == random_number:
            bot.reply_to(message, "Well done, you guessed right!")
        elif input_user < random_number:
            bot.reply_to(message, "The random number is larger.")
        elif input_user > random_number:
            bot.reply_to(message, "The random number is smaller.")

bot.polling()
