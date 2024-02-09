from telebot import TeleBot

TOKEN = 'TU_TOKEN_AQUÍ'
USER_ID = '64329279473'

bot = TeleBot(TOKEN)

@bot.message_handler(func=lambda message: message.from_user.id == USER_ID)
def handle_message(message):
    # Aquí va tu código para ejecutar cuando recibas un mensaje del usuario específico
    print(f'Mensaje recibido de {message.from_user.username}: {message.text}')

bot.polling()
