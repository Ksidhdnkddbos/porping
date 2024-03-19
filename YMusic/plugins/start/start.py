from pyrogram import filters
from YMusic import app
import config
from filters import command


START_COMMAND = ["الاوامر", "ST"]

@app.on_message(command(START_COMMAND)
	)
async def _start(_, message):
	await message.reply_text("""-› اليك قائمة الأوامر - تم انشاء هذا السورس من قبل @lx5x5

-› تشغيل او شغل ~ تشغيل ملف صوتي في المجموعة
-› تكرار ~ سيقوم تكرار الملف 100 مرة 
-› تخطي او سكب ~ تخطي الملف الصوتي أونلاين 
-› فيديو ~  تشغيل ملف فيديو في المجموعة
-› فيد ~ تنزيل ملف فيديو بحث

~ مطور السورس @Lx5x5 . """)
