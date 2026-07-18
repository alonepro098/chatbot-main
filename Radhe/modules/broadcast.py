import asyncio
import traceback
from pyrogram import filters, Client
from pyrogram.types import Message
from pyrogram.errors import (
    FloodWait,
    InputUserDeactivated,
    UserIsBlocked,
    PeerIdInvalid,
)

from config import OWNER_ID
from Radhe import OWNER, Radhe
from Radhe.database import get_served_chats, get_served_users, get_chats, get_users


async def send_msg(user_id, message):
    try:
        await message.copy(chat_id=user_id)
        return 200, None
    except FloodWait as e:
        await asyncio.sleep(e.value)
        return await send_msg(user_id, message)
    except InputUserDeactivated:
        return 400, f"{user_id} : deactivated\n"
    except UserIsBlocked:
        return 400, f"{user_id} : blocked the bot\n"
    except PeerIdInvalid:
        return 400, f"{user_id} : user id invalid\n"
    except Exception:
        return 500, f"{user_id} : {traceback.format_exc()}\n"


@Radhe.on_cmd("br")
async def broadcast(_, message: Message):
    # Check if the sender is the owner
    if message.from_user.id != OWNER:
        return await message.reply_text("😏 **ʏσυ ¢αη'τ υѕє τнιѕ ¢σммαη∂**")

    if not message.reply_to_message:
        await message.reply_text("ʀᴇᴘʟʏ ᴛᴏ ᴀ ᴍᴇssᴀɢᴇ ᴛᴏ ʙʀᴏᴀᴅᴄᴀsᴛ ɪᴛ.")
        return    

    exmsg = await message.reply_text("sᴛᴀʀᴛᴇᴅ ʙʀᴏᴀᴅᴄᴀsᴛɪɴɢ!")
    all_chats = await get_chats()
    all_users = await get_users()
    
    done_chats = 0
    done_users = 0
    failed_chats = 0
    failed_users = 0

    for chat in all_chats:
        try:
            status, _ = await send_msg(chat, message.reply_to_message)
            if status == 200:
                done_chats += 1
            else:
                failed_chats += 1
            await asyncio.sleep(0.1)
        except Exception:
            failed_chats += 1

    for user in all_users:
        try:
            status, _ = await send_msg(user, message.reply_to_message)
            if status == 200:
                done_users += 1
            else:
                failed_users += 1
            await asyncio.sleep(0.1)
        except Exception:
            failed_users += 1

    if failed_users == 0 and failed_chats == 0:
        await exmsg.edit_text(
            f"**sᴜᴄᴄᴇssғᴜʟʟʏ ʙʀᴏᴀᴅᴄᴀsᴛɪɴɢ ✅**\n\n"
            f"**sᴇɴᴛ ᴍᴇssᴀɢᴇ ᴛᴏ** `{done_chats}` **ᴄʜᴀᴛs ᴀɴᴅ** `{done_users}` **ᴜsᴇʀs**"
        )
    else:
        await exmsg.edit_text(
            f"**sᴜᴄᴄᴇssғᴜʟʟʏ ʙʀᴏᴀᴅᴄᴀsᴛɪɴɢ ✅**\n\n"
            f"**sᴇɴᴛ ᴍᴇssᴀɢᴇ ᴛᴏ** `{done_chats}` **ᴄʜᴀᴛs** `{done_users}` **ᴜsᴇʀs**\n\n"
            f"**ɴᴏᴛᴇ:-** `ᴅᴜᴇ ᴛᴏ sᴏᴍᴇ ɪssᴜᴇ ᴄᴀɴ'ᴛ ᴀʙʟᴇ ᴛᴏ ʙʀᴏᴀᴅᴄᴀsᴛ` "
            f"`{failed_users}` **ᴜsᴇʀs ᴀɴᴅ** `{failed_chats}` **ᴄʜᴀᴛs**"
        )


@Radhe.on_cmd("an")
async def announced(client: Client, message: Message):
    # Check if the sender is the owner
    if message.from_user.id != OWNER:
        return await message.reply_text("😏 **ʏσυ ¢αη'τ υѕє τнιѕ ¢σммαη∂**")

    if message.reply_to_message:
        to_send = message.reply_to_message.id
    else:
        return await message.reply_text("Reply To Some Post To Broadcast")

    chats = await get_chats()
    users = await get_users()

    failed = 0
    for chat in chats:
        try:
            await client.forward_messages(
                chat_id=int(chat),
                from_chat_id=message.chat.id,
                message_ids=to_send
            )
            await asyncio.sleep(1)
        except Exception:
            failed += 1

    failed_user = 0
    for user in users:
        try:
            await client.forward_messages(
                chat_id=int(user),
                from_chat_id=message.chat.id,
                message_ids=to_send
            )
            await asyncio.sleep(1)
        except Exception:
            failed_user += 1

    await message.reply_text(
        "Bʀᴏᴀᴅᴄᴀsᴛ ᴄᴏᴍᴘʟᴇᴛᴇ. {} ɢʀᴏᴜᴘs ғᴀɪʟᴇᴅ ᴛᴏ ʀᴇᴄᴇɪᴠᴇ ᴛʜᴇ ᴍᴇssᴀɢᴇ, "
        "ᴘʀᴏʙᴀʙʟʏ ᴅᴜᴇ ᴛᴏ ʙᴇɪɴɢ ᴋɪᴄᴋᴇᴅ. {} ᴜsᴇʀs ғᴀɪʟᴇᴅ ᴛᴏ ʀᴇᴄᴇɪᴠᴇ ᴛʜᴇ ᴍᴇssᴀɢᴇ, "
        "ᴘʀᴏʙᴀʙʟʏ ᴅᴜᴇ ᴛᴏ ʙᴇɪɴɢ ʙᴀɴɴᴇᴅ."
        .format(failed, failed_user)
    )
