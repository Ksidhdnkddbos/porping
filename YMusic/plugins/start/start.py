from pyrogram import filters
from YMusic import app
import config
from filters import command


START_COMMAND = ["الاوامر", "ST"]

@app.on_message(command(START_COMMAND)
	)
async def _start(_, message):
	await message.reply_text("""-› ◥ اެواެمـݛ اެݪتشغيݪ ◤

-› تشغيل/شغلㅤ~ㅤݪـ تشغيݪ اެلاغَنية باެلاتصاݪ  .
-› فيد/فيديوㅤ~  ݪـ تشغيݪ مقطع فديو باެلاتصاݪ .

-› تكرارㅤ~ㅤݪـ تكݛاެݛ اެلاغَنية 100 مݛه .
-› انهاءㅤ~ㅤݪـ اެنهاء اݪتكݛاެݛ .
-› تخطي/سكبㅤ~ㅤݪـ تخطي اެلاغَنية .

-› كتمㅤ~ㅤݪـ كتم اެلاغَنية .
-› رفعㅤ~ㅤݪـ ݛفع الكتم .

-› ايقافㅤ~ㅤݪـ اެيقاف اެݪتشغيݪ .

◥ مطـوݛ اެݪسـوݛس ~ @Lx5x5 ◤ .""")
