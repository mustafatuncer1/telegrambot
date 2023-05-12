import telegram
import requests
from telegram import Bot
import time
from telegram.ext import Updater, CommandHandler
from bs4 import BeautifulSoup

# Telegram bot token'ı
TOKEN = '6018757450:AAEeTqaeNOMl5yh1-WX9bKxx9DrIx-ZOWrQ'

# Chat ID'niz
CHAT_ID = '1538458017'

# Kontrol edilecek web sayfasının URL'si
URL = "https://www.akakce.com/islemci-sogutucu/en-ucuz-arctic-freezer-50-tr-rgb-cpu-sogutucu-fiyati,566619894.html"

# Belirli bir aralıkta kontrol etmek için uyku süresi (saniye cinsinden)
SLEEP_TIME = 60 * 60 * 24  # 24 saat

# En düşük fiyatı kontrol etmek için fonksiyon

def get_min_price():
    HEADERS = ({
        'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit / 537.36(KHTML, like Gecko) Chrome / 44.0.2403.157 Safari / 537.36',
        'Accept-Language': 'en-US, en;q=0.5'})
    webpage = requests.get(URL, headers=HEADERS)
    soup = BeautifulSoup(webpage.content, "lxml")
    # Belirli bir etiket ve sınıftaki metni alın
    result = soup.find('span', class_='pt_v8').text
    return result

# Telegram mesajı göndermek için fonksiyon
def send_telegram_message(message):
    bot = Bot(token='6018757450:AAEeTqaeNOMl5yh1-WX9bKxx9DrIx-ZOWrQ')
    bot.send_message(chat_id='1538458017', text=message)

# /sogutucu komutunu işlemek için fonksiyon
def handle_sogutucu_command(update, context):
    #Gelen komutu console'a yazdır
    #print(f"Gelen komut: {update.message.text}")
    min_price = get_min_price()
    message = "En düşük fiyat: {}".format(min_price)
    print(message)
    send_telegram_message(message)


# Telegram bot nesnesi oluştur
bot = telegram.Bot(token=TOKEN)

# Updater nesnesi oluştur
updater = Updater(token=TOKEN, use_context=True)

# /sogutucu komutu için komut işleyicisini bot nesnesine ekleyin
updater.dispatcher.add_handler(CommandHandler('sogutucu', handle_sogutucu_command))

# Botu başlatın
updater.start_polling()
updater.idle()
