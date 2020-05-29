from telethon import events
import asyncio
import os
import sys
from uniborg.util import admin_cmd

@borg.on(admin_cmd(pattern=r"tsend ?(.*)", allow_sudo=True))
async def test(event):
    if event.reply_to_msg_id:
    	message_id = event.reply_to_msg_id
    msg = event.pattern_match.group(1)
    await borg.send_message(
                    event.chat_id, "{}".format(msg), reply_to=message_id)