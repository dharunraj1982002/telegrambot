import telebot
import openai
import os
from PIL import Image
from pytesseract import pytesseract

# set the API key for openai
openai.api_key = "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"
bot = telebot.TeleBot('6050716393:AAF8uasw_EM-NaFg25d6_616k6pRAO-ZBBo')

@bot.message_handler(content_types=['photo','document','file'])
def handle_photo(message):
    if message.photo:
        print("image received")
        bot.reply_to(message, "Please wait processing your image")
        photo_id = message.photo[-1].file_id
        file_path = bot.get_file(photo_id).file_path

    # Extract the file extension from the file path
        file_extension = os.path.splitext(file_path)[-1]

    # Download the photo to your local directory with the original name
        downloaded_file = bot.download_file(file_path)
        file_name = f"received_photo{file_extension}"
        with open(file_name, 'wb') as f:
            f.write(downloaded_file)
            # Get the path of the downloaded file
        file_path = os.path.join(os.getcwd(), file_name)
        path_to_tesseract = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
        pytesseract.tesseract_cmd = path_to_tesseract
        path_to_image = file_path
        img = Image.open(path_to_image)
        text = pytesseract.image_to_string(img)
        bot.reply_to(message, text)
    elif message.document:
        print("doc received")
        bot.reply_to(message, "Please wait processing your image")
        photo_id = message.document.file_id
        file_path = bot.get_file(photo_id).file_path

    # Extract the file extension from the file path
        file_extension = os.path.splitext(file_path)[-1]

    # Download the photo to your local directory with the original name
        downloaded_file = bot.download_file(file_path)
        file_name = f"received_photo{file_extension}"
        with open(file_name, 'wb') as f:
            f.write(downloaded_file)
            # Get the path of the downloaded file
        file_path = os.path.join(os.getcwd(), file_name)
        path_to_tesseract = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
        pytesseract.tesseract_cmd = path_to_tesseract
        path_to_image = file_path
        img = Image.open(path_to_image)
        text = pytesseract.image_to_string(img)
        bot.reply_to(message, text)

@bot.message_handler(func=lambda message: True)
def echo_message(message):
    cid = message.chat.id
    mid = message.message_id
    message_text = message.text
    user_id = message.from_user.id
    user_name = message.from_user.first_name
    print(cid,mid,message_text,user_id,user_name)
  

    
    if(message_text=="/start"):
        bot.reply_to(message, "Hello "+user_name+"! Welcome to my bot.\n /help")
    elif(message_text=="/hello"):
        bot.reply_to(message, "Hello there! ITs me LINDR bot")
    elif(message_text=="/info"):
        bot.reply_to(message, "I'm a simple bot in the beginning stage. Just let me know what you expect from me to perform")
    elif(message_text=="/convert"):
        #Define path to tessaract.exe
        #path_to_tesseract = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
        bot.reply_to(message,"send the image")
        
        
        #Define path to image
        '''photo_id = message.photo[-1].file_id
        file_path = bot.get_file(photo_id).file_path
        downloaded_file = bot.download_file(file_path)
        with open('photo.jpg', 'wb') as f:
            f.write(downloaded_file)
        path_to_image = file_path
        pytesseract.tesseract_cmd = path_to_tesseract
        img = Image.open(path_to_image)
        text = pytesseract.image_to_string(img)
        path_to_image = 'cursiveimg.jpg'
        #Point tessaract_cmd to tessaract.exe
        pytesseract.tesseract_cmd = path_to_tesseract
        #Open image with PIL
        img = Image.open(path_to_image)
        #Extract text from image
        text = pytesseract.image_to_string(img)
        #bot.reply_to(message, "Working on it")
        bot.reply_to(message, text)'''
    elif(message_text=="/help"):
        commands = ['/start - Start the bot', '/hello - Say hello', '/info - Show bot information','/convert- image to text', '/help - Show available commands']
        commands_text = '\n'.join(commands)
        bot.reply_to(message, f"Available commands:\n{commands_text}")
    elif(message_text.startswith("hi" or "hello")):
        bot.reply_to(message,"Hi "+user_name+" How are you doing?")
    elif(message_text.startswith("fine") or message_text.startswith("Fine") or message_text.startswith("good") or message_text.startswith("Good")):
        bot.reply_to(message,"Okay "+user_name+" How can I help You")
    else:
        prompt = (message_text)
        # generate text with the prompt
        generated_text = openai.Completion.create(
        engine="text-davinci-002",
        prompt=prompt,
        max_tokens=1024,
        n=1,
        stop=None,
        temperature=0.5,
    )
        bot.reply_to(message, generated_text["choices"][0]["text"]+"\n"+"/help ")
#bot.add_message_handler(echo_message)
#bot.add_message_handler(handle_photo)
bot.polling()
