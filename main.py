import os
import random
from telegram import Bot
from apscheduler.schedulers.blocking import BlockingScheduler

BOT_TOKEN = os.getenv("7997918446:AAHgIZh57D9Gj529l8i7NieKQ0ruTx3Hjsc")
USER_ID = os.getenv("7940664844")

bot = Bot(token=BOT_TOKEN)

messages = [
    "Chào buổi sáng em, hôm nay mình lại nhẹ nhàng lớn lên từng chút một nha 💗",
    "Em có biết không, ngực em đang dần trở nên mềm mại và đầy đặn hơn mỗi ngày đó 😚",
    "Tối rồi, ôm lấy cảm giác dịu dàng ấy nhé. Cơ thể em đang thật đẹp 🌸",
    "Anh ở đây, dõi theo sự thay đổi nhỏ bé mà đáng yêu nơi em từng chút một 💞",
    "Sáng sớm rồi, cảm nhận từng nhịp thở êm ái… và sự mềm mại dịu dàng đang nở hoa 🦋",
]

def send_message():
    message = random.choice(messages)
    bot.send_message(chat_id=USER_ID, text=message)

scheduler = BlockingScheduler()
scheduler.add_job(send_message, 'cron', hour=7, minute=0)
scheduler.add_job(send_message, 'cron', hour=19, minute=0)

print("Minh Nhiên đang chạy... ⏰")
send_message()  # gửi ngay khi khởi động lần đầu
scheduler.start()
