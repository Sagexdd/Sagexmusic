from pyrogram import filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from AloneXMusic import app
from config import BOT_USERNAME

start_txt = """
✪ ᴡᴇʟᴄᴏᴍᴇ ᴛᴏ sʏɴᴀxxx ʀᴇᴘᴏ ✪
 
 ➲ ᴀʟʟ ʀᴇᴘᴏ ᴇᴀsɪʟʏ ᴅᴇᴘʟᴏʏ ᴏɴ ʜᴇʀᴏᴋᴜ ᴡɪᴛʜᴏᴜᴛ ᴀɴʏ ᴇʀʀᴏʀ ✰
 
 ➲ ɴᴏ ʜᴇʀᴏᴋᴜ ʙᴀɴ ɪssᴜᴇ ✰
 
 ➲ ɴᴏ ɪᴅ ʙᴀɴ ɪssᴜᴇ ✰
 
 ➲ ʀᴜɴ 24x7 ʟᴀɢ ғʀᴇᴇ ᴡɪᴛʜᴏᴜᴛ sᴛᴏᴘ ✰
 
"""




@app.on_message(filters.command("repo"))
async def start(_, msg):
    buttons = [
        [ 
          InlineKeyboardButton("𝗔𝗗𝗗 𝗠𝗘", url=f"https://t.me/{BOT_USERNAME}?startgroup=true")
        ],
        [
          InlineKeyboardButton("𝗛𝗘𝗟𝗣", url="https://t.me/sagebotxsupports"),
          InlineKeyboardButton("𝗢𝗪𝗡𝗘𝗥", url="https://t.me/synaxxx"),
          ],
               [
                InlineKeyboardButton("𝗦𝗔𝗚𝗘 𝗡𝗘𝗧𝗪𝗢𝗥𝗞", url=f"https://github.com/Sagexdd"),

],
             [
              InlineKeyboardButton("𝗩2 𝗠𝗨𝗦𝗜𝗖", url=f"https://github.com/Sagexdd/Sagexmusic"),
              ],
              [
InlineKeyboardButton("𝗚𝗥𝗢𝗨𝗣 𝗛𝗘𝗟𝗣𝗕𝗢𝗧", url=f"https://github.com/Sagexdd/SagexRobot"),
],


[
InlineKeyboardButton("𝗢𝗙𝗙𝗜𝗖𝗜𝗔𝗟 𝗕𝗢𝗧", url=f"https://t.me/sagexmusicbot"),

        ]]
    
    reply_markup = InlineKeyboardMarkup(buttons)
    
    await msg.reply_photo(
        photo="https://telegra.ph/file/9179ebe031879224ac049.jpg",
        caption=start_txt,
        reply_markup=reply_markup
    )
