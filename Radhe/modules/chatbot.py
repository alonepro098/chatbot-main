import random
from Abg.chat_status import adminsOnly

from pyrogram import Client, filters
from pyrogram.enums import ChatAction
from pyrogram.types import InlineKeyboardMarkup, Message

from Radhe import Radhe, mongo
from Radhe.database import RADHE
from Radhe.modules.helpers import CHATBOT_ON


@Radhe.on_cmd("chatbot", group_only=True)
@adminsOnly("can_delete_messages")
async def chaton_(_, m: Message):
    await m.reply_text(
        f"ᴄʜᴀᴛ: {m.chat.title}\n**ᴄʜᴏᴏsᴇ ᴀɴ ᴏᴩᴛɪᴏɴ ᴛᴏ ᴇɴᴀʙʟᴇ/ᴅɪsᴀʙʟᴇ ᴄʜᴀᴛʙᴏᴛ.**",
        reply_markup=InlineKeyboardMarkup(CHATBOT_ON),
    )


@Radhe.on_message(
    (filters.text | filters.sticker) & ~filters.private & ~filters.bot,
    group=4,
)
async def chatbot_group(client: Client, message: Message):
    try:
        if message.text and message.text.startswith(("!", "/", "?", "@", "#")):
            return
    except Exception:
        pass

    if mongo is None or RADHE is None:
        return

    # Check if chatbot is disabled in this group
    is_RADHE = await RADHE.find_one({"chat_id": message.chat.id})
    if is_RADHE:
        return

    chatai = mongo["Word"]["WordDb"]

    # Learn from replies between other users (not bot itself)
    if (
        message.reply_to_message
        and message.reply_to_message.from_user
        and message.reply_to_message.from_user.id != client.id
    ):
        replied_msg = message.reply_to_message
        if replied_msg.text:
            word_to_learn = replied_msg.text.strip()
            
            # Learn sticker reply
            if message.sticker:
                existing = await chatai.find_one(
                    {
                        "word": word_to_learn,
                        "id": message.sticker.file_unique_id,
                    }
                )
                if not existing:
                    await chatai.insert_one(
                        {
                            "word": word_to_learn,
                            "text": message.sticker.file_id,
                            "check": "sticker",
                            "id": message.sticker.file_unique_id,
                        }
                    )
            
            # Learn text reply
            elif message.text:
                existing = await chatai.find_one(
                    {"word": word_to_learn, "text": message.text.strip()}
                )
                if not existing:
                    await chatai.insert_one(
                        {
                            "word": word_to_learn,
                            "text": message.text.strip(),
                            "check": "none",
                        }
                    )
        return

    # Reply logic (Not a reply OR reply to the bot itself)
    lookup_word = None
    if message.text:
        lookup_word = message.text.strip()
    elif message.sticker:
        lookup_word = message.sticker.file_unique_id

    if not lookup_word:
        return

    is_reply_to_bot = (
        message.reply_to_message
        and message.reply_to_message.from_user
        and message.reply_to_message.from_user.id == client.id
    )

    if not message.reply_to_message or is_reply_to_bot:
        cursor = chatai.find({"word": lookup_word})
        data = await cursor.to_list(length=100)
        if data:
            await client.send_chat_action(message.chat.id, ChatAction.TYPING)
            pick = random.choice(data)
            if pick.get("check") == "sticker":
                await message.reply_sticker(pick["text"])
            else:
                await message.reply_text(pick["text"])


@Radhe.on_message(
    (filters.text | filters.sticker) & filters.private & ~filters.bot,
    group=4,
)
async def chatbot_private(client: Client, message: Message):
    try:
        if message.text and message.text.startswith(("!", "/", "?", "@", "#")):
            return
    except Exception:
        pass

    if mongo is None:
        return

    chatai = mongo["Word"]["WordDb"]

    lookup_word = None
    if message.text:
        lookup_word = message.text.strip()
    elif message.sticker:
        lookup_word = message.sticker.file_unique_id

    if not lookup_word:
        return

    cursor = chatai.find({"word": lookup_word})
    data = await cursor.to_list(length=100)
    if data:
        await client.send_chat_action(message.chat.id, ChatAction.TYPING)
        pick = random.choice(data)
        if pick.get("check") == "sticker":
            await message.reply_sticker(pick["text"])
        else:
            await message.reply_text(pick["text"])
