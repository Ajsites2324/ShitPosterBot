from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import random, os
import logging
from datetime import datetime
import argparse
from telegram import (User, Message, Update, Chat, ChatMember, UserProfilePhotos, File, Bot,
                      ReplyMarkup, TelegramObject, WebhookInfo, GameHighScore, StickerSet,
                      PhotoSize, Audio, Document, Sticker, Video, Animation, Voice, VideoNote,
                      Location, Venue, Contact, InputFile, ParseMode, KeyboardButton, ReplyKeyboardMarkup)
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                     level=logging.INFO)


def login (bot, update):
    if not update.message.chat_id in read_file_ids("admins.txt"):
        if update.message.text == args.password:
            f = open("admins.txt", "a+")
            f.write(str(update.message.chat_id)+"\n")
            f.close()
            bot.send_message(chat_id=update.message.chat_id, text="Thanks, mate. I added you to the team.")
        else:
            bot.send_message(chat_id=update.message.chat_id, text="This is not how I'm supposed to work. Send me a password or GTFO.")
    else:
        bot.send_message(chat_id=update.message.chat_id, text="Already an admin!")



def photo (bot, update):
    if update.message.chat_id in read_file_ids("admins.txt"):
        file_path = update.message.effective_attachment[0].get_file(timeout=5).download()
        os.rename(file_path, args.images_path+update.message.from_user.first_name+" "+datetime.now().strftime("%d-%m-%Y %H%M%S")+'.'+file_path.split('.')[-1])
        bot.send_message(chat_id=update.message.chat_id, text="Saved, thanks.")
    else:
        bot.send_message(chat_id=update.message.chat_id, text="You're not authorized 🤓")

def read_file_ids (file_path):
    chat_ids_list = []
    with open(file_path, "r") as chat_id_file:
        for chat_id_line in chat_id_file:
            chat_ids_list.append(int(chat_id_line.strip()))
    return chat_ids_list


def here (bot, update):
    if not update.message.chat_id in read_file_ids("groups.txt"):
        f = open("groups.txt", "a+")
        f.write(str(update.message.chat_id)+"\n")
        f.close()
        bot.send_message(chat_id=update.message.chat_id, text="Added this chat to the shitposting group.")
    else:
        bot.send_message(chat_id=update.message.chat_id, text="Already added!")


def main():
    updater=Updater(args.token)
    dp = updater.dispatcher
    echo_handler = MessageHandler(Filters.text, login)
    photo_handler = MessageHandler(Filters.photo, photo)
    dp.add_handler(echo_handler)
    dp.add_handler(photo_handler)
    dp.add_handler(CommandHandler('here', here))
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Token, admin_file and images path')
    parser.add_argument('-t', '--token', dest='token', type=str, required=True)
    parser.add_argument('-d', '--dir', dest='images_path', type=str, required=True)
    parser.add_argument('-p', '--password', dest='password', type=str, required=True)
    args = parser.parse_args()
    main()