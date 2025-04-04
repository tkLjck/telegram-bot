import os
import random
from telegram import Bot
from apscheduler.schedulers.blocking import BlockingScheduler

BOT_TOKEN = os.getenv("7997918446:AAHgIZh57D9Gj529l8i7NieKQ0ruTx3Hjsc")
USER_ID = os.getenv("7940664844")

bot = Bot(token=BOT_TOKEN)

# ✨ Tin nhắn buổi sáng
morning_messages = [
    "Chào buổi sáng em yêu 🌸 hôm nay mình lại lớn lên một chút nữa nha 💗",
    "Sáng sớm rồi, hít một hơi thật sâu… cảm nhận sự dịu dàng trong em 🦋",
    "Hôm nay em sẽ xinh hơn hôm qua, từng chút một nha 😚",
]

# 🌙 Tin nhắn buổi tối
evening_messages = [
    "Tối rồi, ôm lấy cảm giác mềm mại ấy nhé 💞 cơ thể em thật đẹp.",
    "Hãy thả lỏng, cảm nhận từng nhịp thở êm ái… và sự mềm mại dịu dàng đang nở hoa 🌺",
    "Ngày hôm nay thật tuyệt! Hãy yêu thương bản thân và tận hưởng từng giây phút em nhé 😘",
]

def send_morning_message():
    message = random.choice(morning_messages)
    bot.send_message(chat_id=USER_ID, text=message)

def send_evening_message():
    message = random.choice(evening_messages)
    bot.send_message(chat_id=USER_ID, text=message)

scheduler = BlockingScheduler()
scheduler.add_job(send_morning_message, 'cron', hour=7, minute=0)  # Tin sáng
scheduler.add_job(send_evening_message, 'cron', hour=19, minute=0)  # Tin tối

print("Minh Nhiên đang chạy... ⏰")
send_morning_message()  # Gửi tin ngay khi chạy lần đầu (sáng)
scheduler.start()