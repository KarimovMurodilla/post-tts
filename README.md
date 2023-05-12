# post-tts
Telegram bot converting text posts into voice


# Info
Telegram kanallardagi postlarni ovozli habar o'giruvchi bot.
> Textni ovozga o'girish uchun Muxlisa api ishlatilgan

# Ishga tushurish
**1. Ushbu repository ni clone qilib olish:**
```
git clone https://github.com/KarimovMurodilla/post-tts.git
```

**2. Kerakli modullarni yuklab olish**
```
pip install -r requirements.txt
```
  
**3. `.env` fayl ochib, unga `ADMINS` va `BOT_TOKEN` variable larnni berish kerak bo'ladi.**

**4. Botni ishga tushurish**
```
python app.py
```

**5. Admin panelni ishga tushurish**

```
uvicorn admin_panel:app --reload
```