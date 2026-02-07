from pyrogram import Client, filters

# بياناتك الخاصة يا ياسر
API_ID = 21437281
API_HASH = "6d8fd92d56b9b9db9377cc493fa641d0"
BOT_TOKEN = "8507472664:AAGQ_xlh-CLwCafVBGp5YPaBOmD_th40q88"

app = Client("yasser_session", api_id=API_ID, api_hash=API_HASH, bot_token=BOT_TOKEN)

@app.on_message(filters.command("start"))
async def start(client, message):
    await message.reply_text("✅ أهلاً يا ياسر! البوت يعمل الآن بنجاح على Render ومستعد للتحليل.")

@app.on_message(filters.regex(r"^تحليل\s(\w+)"))
async def analyze(client, message):
    coin = message.matches[0].group(1).upper()
    await message.reply_text(f"📊 تحليل عملة #{coin}USDT\nالقرار: بناءً على استراتيجية EMA 50 و RSI 78/22.")

app.run()
