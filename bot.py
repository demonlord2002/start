from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton

# Replace with your API credentials
API_ID = 22201946
API_HASH = "f4e7f0de47a09671133ecafa6920ebbe"
BOT_TOKEN = "7945536495:AAGQhAa6BDfg8kgQ77Ga4Jsh4arODyHrhb4"

bot = Client(
    "CoolieMovieBot",
    api_id=API_ID,
    api_hash=API_HASH,
    bot_token=BOT_TOKEN
)

CHANNEL_LINK = "https://t.me/+1A5SxtZArxkxZDVl"
START_IMAGE = "https://graph.org/file/ef913ae481b78227404ec-c2fe746f3a25c938ba.jpg"

@bot.on_message(filters.command("start") & filters.private)
async def start_handler(client, message):
    start_text = (
        "╭───────────────────╮\n"
        "    ✨ **𝙲𝚘𝚘𝚕𝚒𝚎 𝙼𝚘𝚟𝚒𝚎 𝙸𝚜 𝙷𝚎𝚛𝚎!** ✨\n"
        "╰───────────────────╯\n\n"
        "> 🍿 **உங்களுக்காக 𝙵𝚒𝚛𝚜𝚝 𝚄𝚙𝚍𝚊𝚝𝚎 வந்தாச்சு!**\n"
        "> 🎬 *Coolie* படம் **Direct Link** ரெடியா இருக்கு...\n"
        "> ⚡ **டவுன்லோட்** பண்ண ரெடி ஆ இருங்க!\n"
        "> 📢 *Upcoming Movies* updates **Miss பண்ணாதீங்க!**\n"
        "> 🔥 **𝙿𝚛𝚒𝚖𝚎𝚄𝚙𝚕𝚘𝚊𝚍𝚣 𝙵𝚒𝚛𝚜𝚝 𝚁𝚎𝚕𝚎𝚊𝚜𝚎!**\n"
    )

    buttons = InlineKeyboardMarkup([
        [
            InlineKeyboardButton("📥 𝗖𝗹𝗶𝗰𝗸 𝗧𝗼 𝗗𝗼𝘄𝗻𝗹𝗼𝗮𝗱", url=CHANNEL_LINK)
        ],
        [
            InlineKeyboardButton("🎬 𝗨𝗽𝗰𝗼𝗺𝗶𝗻𝗴 𝗠𝗼𝘃𝗶𝗲𝘀", url=CHANNEL_LINK)
        ]
    ])

    sent = await message.reply_photo(
        photo=START_IMAGE,
        caption=start_text,
        reply_markup=buttons
    )

    # Add a 🔥 reaction to the bot's own message (Pyrogram v2.0+)
    try:
        await bot.send_reaction(
            chat_id=message.chat.id,
            message_id=sent.id,
            emoji="🔥"
        )
    except:
        pass  # Ignore if reactions aren't supported

print("Bot is running...")
bot.run()
