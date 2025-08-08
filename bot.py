import random
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
    bot_token=BOT_TOKEN,
    parse_mode="html"  # ✅ Set parse mode here (lowercase is fine)
)

CHANNEL_LINK = "https://t.me/+1A5SxtZArxkxZDVl"
START_IMAGE = "https://graph.org/file/ef913ae481b78227404ec-c2fe746f3a25c938ba.jpg"

REACTION_EMOJIS = ["🔥", "😎", "💥", "❤️", "🎯", "⚡", "🤩", "🥳", "💎"]

@bot.on_message(filters.command("start"))
async def start_handler(client, message):
    random_emoji = random.choice(REACTION_EMOJIS)
    emoji_suffix = f" {random_emoji}" if message.chat.type == "private" else ""

    start_text = (
        f"<blockquote><b><u>╭───────────────────╮\n"
        f"✨ 𝙲𝚘𝚘𝚕𝚒𝚎 𝙼𝚘𝚟𝚒𝚎 𝙸𝚜 𝙷𝚎𝚛𝚎! ✨{emoji_suffix}\n"
        f"╰───────────────────╯</u></b></blockquote>\n\n"
        f"<blockquote>🍿 <b>உங்களுக்காக 𝙵𝚒𝚛𝚜𝚝 𝚄𝚙𝚍𝚊𝚝𝚎 வந்தாச்சு!</b></blockquote>\n"
        f"<blockquote>🎬 <i>Coolie</i> படம் <b>Direct Link</b> ரெடியா இருக்கு...</blockquote>\n"
        f"<blockquote>⚡ <b>டவுன்லோட்</b> பண்ண ரெடி ஆ இருங்க!</blockquote>\n"
        f"<blockquote>📢 <i>Upcoming Movies</i> updates <b>Miss பண்ணாதீங்க!</b></blockquote>\n"
        f"<blockquote>🔥 <b>𝙿𝚛𝚒𝚖𝚎𝚄𝚙𝚕𝚘𝚊𝚍𝚣 𝙵𝚒𝚛𝚜𝚝 𝚁𝚎𝚕𝚎𝚊𝚜𝚎!</b></blockquote>"
    )

    buttons = InlineKeyboardMarkup([
        [InlineKeyboardButton("📥 𝗖𝗹𝗶𝗰𝗸 𝗧𝗼 𝗗𝗼𝘄𝗻𝗹𝗼𝗮𝗱", url=CHANNEL_LINK)],
        [InlineKeyboardButton("🎬 𝗨𝗽𝗰𝗼𝗺𝗶𝗻𝗴 𝗠𝗼𝘃𝗶𝗲𝘀", url=CHANNEL_LINK)]
    ])

    sent = await message.reply_photo(
        photo=START_IMAGE,
        caption=start_text,
        reply_markup=buttons
    )

    if message.chat.type != "private":
        try:
            await bot.send_reaction(
                chat_id=message.chat.id,
                message_id=sent.id,
                emoji=random_emoji
            )
        except:
            pass

print("Bot is running...")
bot.run()
