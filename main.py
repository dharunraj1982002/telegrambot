import telebot

bot = telebot.TeleBot('6050716393:AAF8uasw_EM-NaFg25d6_616k6pRAO-ZBBo')

@bot.message_handler(func=lambda message: True)
def echo_message(message):
    cid = message.chat.id
    mid = message.message_id
    message_text = message.text
    user_id = message.from_user.id
    user_name = message.from_user.first_name
    print(cid,mid,message_text,user_id,user_name)
    if(user_name=="Vishalini" or user_name.startswith("Vish")):
        if(message_text=="/start"):
            bot.reply_to(message, "Hello "+user_name+"! Welcome to my bot.")
            bot.reply_to(message,"Many more happy returns of the day🤩🤗\n")
            bot.reply_to(message,"Iniya pirandha naal vaazhthukkal(●'◡'●)\n")
            bot.reply_to(message,"Putinaroju subakankshalu😌💕\n")
            bot.reply_to(message,"Have a happiest and beautiful year ahead🫶\n\n/help")

        elif(message_text=="/hello"):
            bot.reply_to(message, "Hello there! ITs me LINDR bot, your assistant😉🫡 🫡 ")
        elif(message_text=="/info"):
            bot.reply_to(message, "I'm a simple bot in the beginning stage. Just let me know what you expect from me to perform")
        elif(message_text=="/bye"):
            bot.reply_to(message,"I need your help for improving myself....🫣 Ok see you later👋")
        elif(message_text=="/help"):
            commands = ['/start - Start the bot', '/hello - Say hello', '/info - Show bot information', '/help - Show available commands','/bye - coversation over']
            commands_text = '\n'.join(commands)
            bot.reply_to(message, f"Available commands:\n{commands_text}")
        elif(message_text.startswith("thank" or "Thank")):
            bot.reply_to(message,"It's my pleasure\nOk Then how was your day?")
        elif(message_text.startswith("hi")or message_text.startswith("hello")):
            bot.reply_to(message,"Hi "+user_name+" How are you doing?")
        elif(message_text.startswith("fine") or message_text.startswith("good") or message_text.startswith("Good") or message_text.startswith("Fine")):
            bot.reply_to(message,"Okay "+user_name+" How can I help You?")
        else:
            bot.reply_to(message,"(not recognized) thank you :) your feedbacks are saved....\nI will get improved soon")
        
    else:
        if(message_text=="/start"):
            bot.reply_to(message, "Hello "+user_name+"! Welcome to my bot.\n /help")
        elif(message_text=="/hello"):
            bot.reply_to(message, "Hello there! ITs me LINDR bot")
        elif(message_text=="/info"):
            bot.reply_to(message, "I'm a simple bot in the beginning stage. Just let me know what you expect from me to perform")
        elif(message_text=="/help"):
            commands = ['/start - Start the bot', '/hello - Say hello', '/info - Show bot information', '/help - Show available commands']
            commands_text = '\n'.join(commands)
            bot.reply_to(message, f"Available commands:\n{commands_text}")
        elif(message_text.startswith("hi" or "hello")):
            bot.reply_to(message,"Hi "+user_name+" How are you doing?")
        elif(message_text.startswith("fine") or message_text.startswith("good") or message_text.startswith("Good")):
            bot.reply_to(message,"Okay "+user_name+" How can I help You")
        else:
            bot.reply_to(message,"thank you :) your feedbacks are saved....\nI will be improving myself")
bot.polling()
