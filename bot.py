from telegram.ext import Updater, CommandHandler
import random, os
import logging
import argparse
from telegram import (User, Message, Update, Chat, ChatMember, UserProfilePhotos, File, Bot,
                      ReplyMarkup, TelegramObject, WebhookInfo, GameHighScore, StickerSet,
                      PhotoSize, Audio, Document, Sticker, Video, Animation, Voice, VideoNote,
                      Location, Venue, Contact, InputFile, ParseMode, KeyboardButton, ReplyKeyboardMarkup)
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                     level=logging.INFO)

def main():
    parser = argparse.ArgumentParser(description='Group chat ID, token and path')
    parser.add_argument('-t', '--token', dest='token', type=str, required=True)
    parser.add_argument('-p', '--path', dest='images_path', type=str, required=True)
    args = parser.parse_args()
    bot = Bot(token=args.token)
    filepath=args.images_path+random.choice(os.listdir(args.images_path))
    with open("groups.txt", "r") as groups:
        for group_chat_id in groups:
            bot.send_photo(chat_id=int(group_chat_id.strip()), photo=open(filepath, 'rb'))
if __name__ == '__main__':    main()