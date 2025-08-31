import logging
import asyncio
from aiogram import Bot, Dispatcher, types
from database import save_user

# Load your bot token (paste yours here)
BOT_TOKEN = "YOUR_TELEGRAM_BOT_TOKEN"

logging.basicConfig(level=logging.INFO)

bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()

# Start command
@dp.message(commands=["start"])
async def cmd_start(message: types.Message):
    save_user(message.from_user.id, message.from_user.username)
    await message.answer("👋 Welcome to CryptoQuiver Bot!\nYour account has been registered in the database ✅")

# Run bot
async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
