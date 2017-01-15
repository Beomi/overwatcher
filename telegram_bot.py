import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "UpdateNoticeBOT.settings")
import django
django.setup()

from django.conf import settings
from datetime import datetime, timedelta

from telegram.ext import Updater, CommandHandler

def start(bot, update):
    telegram_id = update.message['chat']['id']

    guest, is_created = Guest.objects.get_or_create(telegram_id=telegram_id)
    guest.save()

    update.message.reply_text(
        'Notice Alert for OVERWATCH Server')

def register(bot, update):
    pass

updater = Updater(settings.TELEGRAM_TOKEN)

updater.dispatcher.add_handler(CommandHandler('start', start))
updater.start_polling()
updater.idle()