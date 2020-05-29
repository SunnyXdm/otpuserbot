"""
.alive 
For all USER
"""
import asyncio
from telethon import events
from telethon.tl.types import ChannelParticipantsAdmins

@borg.on(events.NewMessage(pattern=r"Bill",incoming=True))
async def _(event):
    if event.fwd_from:
        return
    mentions = "`Well! Well! Well! Well!`"
    chat = await event.get_input_chat()
    async for x in borg.iter_participants(chat, filter=ChannelParticipantsAdmins):
        mentions += f""
    reply_message = None
    if event.reply_to_msg_id:
        reply_message = await event.get_reply_message()
        await reply_message.reply(mentions)
    else:
        await event.reply(mentions)
