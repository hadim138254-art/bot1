from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, ContextTypes, filters

# ======== توکن ربات خودت را اینجا جایگزین کن ========
TOKEN = "8499925053:AAG3k3fv5m57JmCzgI4kQBjSXjJg-i7SpW4"

# ======== دیتای آموزشی ========
FAKE_DATA = [
    {
        "name": "علی",
        "family": "رضایی",
        "national_id": "1111111111",
        "phone": "09120000000",
        "telegram_id": "@ali_test",
        "description": "دیتای آموزشی"
    },
    {
        "name": "سارا",
        "family": "محمدی",
        "national_id": "2222222222",
        "phone": "09350000000",
        "telegram_id": "@sara_test",
        "description": "کاربر تست"
    }
]

# ======== فرمان /start ========
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "🤖 ربات جستجوی اطلاعات آموزشی\n\n"
        "🔎 نام، فامیلی، کد ملی، شماره تماس یا آیدی تلگرام را ارسال کن."
    )

# ======== جستجوی هوشمند ========
def smart_search(query: str):
    query = query.lower()
    results = []

    for person in FAKE_DATA:
        for value in person.values():
            if query in str(value).lower():
                results.append(person)
                break

    return results

# ======== پردازش پیام های متنی ========
async def handle_text(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.message.text.strip()
    results = smart_search(query)

    if not results:
        await update.message.reply_text("❌ موردی پیدا نشد")
        return

    for person in results:
        msg = (
            f"👤 نام: {person['name']}\n"
            f"👤 فامیلی: {person['family']}\n"
            f"🆔 کد ملی: {person['national_id']}\n"
            f"📞 شماره تماس: {person['phone']}\n"
            f"💬 آیدی تلگرام: {person['telegram_id']}\n"
            f"ℹ️ توضیحات: {person['description']}"
        )
        await update.message.reply_text(msg)

# ======== اجرای ربات ========
def main():
    app = ApplicationBuilder().token(TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_text))
    app.run_polling()

# ======== نقطه شروع صحیح ========
if __name__ == "__main__":
    main()