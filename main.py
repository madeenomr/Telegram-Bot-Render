import telebot
from keep_alive import keep_alive # استدعاء ملف الإنعاش
import time

# --- منطقة الإعدادات ---
# ضع التوكن الخاص بك هنا بدلاً من النص الموجود بين علامات التنصيص
TOKEN = "8359787741:AAEjMgEBUulE44MI8sFWCbpFuA8Z-xN3GIY" 

bot = telebot.TeleBot(TOKEN)

# --- أوامر البوت ---

@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "أهلاً بك! أنا بوت تحميل الفيديوهات. أرسل لي الرابط.")

# ... (ضع هنا بقية أكواد وأوامر بوتك الخاصة بالتحميل) ...

# --- تشغيل السيرفر والبوت ---
keep_alive() # تشغيل السيرفر الوهمي أولاً

# حلقة تشغيل البوت
print("Bot is running...")
bot.infinity_polling()
