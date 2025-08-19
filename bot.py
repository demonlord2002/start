from pyrogram.enums import ParseMode
import random
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton

API_ID = 22201946
API_HASH = "f4e7f0de47a09671133ecafa6920ebbe"
BOT_TOKEN = "7945536495:AAGQhAa6BDfg8kgQ77Ga4Jsh4arODyHrhb4"

bot = Client(
    "CoolieMovieBot",
    api_id=API_ID,
    api_hash=API_HASH,
    bot_token=BOT_TOKEN,
    parse_mode=ParseMode.HTML
)

CHANNEL_LINK = "https://t.me/+WkEkiXTAoJM3OTA1"
START_IMAGE = "https://graph.org/file/ef913ae481b78227404ec-c2fe746f3a25c938ba.jpg"

REACTION_EMOJIS = ["🔥", "😎", "💥", "❤️", "🎯", "⚡", "🤩", "🥳", "💎"]

@bot.on_message(filters.command("start"))
async def start_handler(client, message):
    random_emoji = random.choice(REACTION_EMOJIS)

    start_text = (
        "<pre>╭───────────────────╮\n"
        f"✨ 𝙲𝚘𝚘𝚕𝚒𝚎 𝙼𝚘𝚟𝚒𝚎 𝙸𝚜 𝙷𝚎𝚛𝚎! ✨ {random_emoji}\n"
        "╰───────────────────╯</pre>\n\n"
        "▌ 🍿 <b>உங்களுக்காக 𝙵𝚒𝚛𝚜𝚝 𝚄𝚙𝚍𝚊𝚝𝚎 வந்தாச்சு!</b>\n"
        "▌ 🎬 <i>Coolie</i> படம் <b>Direct Link</b> ரெடியா இருக்கு...\n"
        "▌ ⚡ <b>டவுன்லோட்</b> பண்ண ரெடி ஆ இருங்க!\n"
        "▌ 📢 <i>Upcoming Movies</i> updates <b>Miss பண்ணாதீங்க!</b>\n"
        "▌ 🔥 <b>𝙿𝚛𝚒𝚖𝚎𝚄𝚙𝚕𝚘𝚊𝚍𝚣 𝙵𝚒𝚛𝚜𝚝 𝚁𝚎𝚕𝚎𝚊𝚜𝚎!</b>"
    )

    buttons = InlineKeyboardMarkup([
        [InlineKeyboardButton("📥 𝗖𝗹𝗶𝗰𝗸 𝗧𝗼 𝗗𝗼𝘄𝗻𝗹𝗼𝗮𝗱", url=CHANNEL_LINK)],
        [InlineKeyboardButton("🎬 𝗨𝗽𝗰𝗼𝗺𝗶𝗻𝗴 𝗠𝗼𝘃𝗶𝗲𝘀", url=CHANNEL_LINK)]
    ])

    # Send main start message
    sent = await message.reply_photo(
        photo=START_IMAGE,
        caption=start_text,
        reply_markup=buttons
    )

    # Fake a "reaction" in private chat by sending just the emoji
    await message.reply_text(random_emoji)

bot.run()
