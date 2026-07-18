from Radhe import db

chatsdb = db.chatsdb if db is not None else None


async def get_served_chats() -> list:
    if chatsdb is None:
        return []
    chats = chatsdb.find({"chat_id": {"$lt": 0}})
    chats_list = []
    async for chat in chats:
        chats_list.append(chat)
    return chats_list


async def is_served_chat(chat_id: int) -> bool:
    if chatsdb is None:
        return False
    chat = await chatsdb.find_one({"chat_id": chat_id})
    return chat is not None


async def add_served_chat(chat_id: int):
    if chatsdb is None:
        return None
    is_served = await is_served_chat(chat_id)
    if is_served:
        return None
    return await chatsdb.insert_one({"chat_id": chat_id})


async def remove_served_chat(chat_id: int):
    if chatsdb is None:
        return None
    is_served = await is_served_chat(chat_id)
    if not is_served:
        return None
    return await chatsdb.delete_one({"chat_id": chat_id})


# Consolidated helper functions from old db/chatsdb.py
async def get_chats() -> list:
    if chatsdb is None:
        return []
    chats_list = []
    async for chat in chatsdb.find({"chat_id": {"$lt": 0}}):
        chats_list.append(chat["chat_id"])
    return chats_list


async def get_chat(chat_id: int) -> bool:
    return await is_served_chat(chat_id)


async def add_chat(chat_id: int):
    await add_served_chat(chat_id)


async def del_chat(chat_id: int):
    await remove_served_chat(chat_id)
